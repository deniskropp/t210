import os
from pathlib import Path
from typing import List, Optional
from uuid import UUID
import aiosqlite
from datetime import datetime, timezone

from src.core.domain.models import Content, Metadata
from src.core.domain.ports import HistoryPort
from src.shared.config import settings

class SQLiteStorage(HistoryPort):
    """
    SQLite implementation of the HistoryPort.
    """

    def __init__(self, db_path: str | None = None) -> None:
        """
        Args:
            db_path: Optional path to the database file. If None, uses XDG default.
        """
        if db_path:
            self.db_path = db_path
        else:
            xdg_data = os.environ.get("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
            base_dir = Path(xdg_data) / "klipper"
            base_dir.mkdir(parents=True, exist_ok=True)
            self.db_path = str(base_dir / settings.DB_PATH)
        
        self._initialized = False
        self._mem_conn: Optional[aiosqlite.Connection] = None

    def _db_context(self):
        """
        Returns a context manager for the database connection.
        Handles persistent connection for :memory: databases.
        """
        if self.db_path == ":memory:":
            class NoCloseContext:
                def __init__(self, parent): self.parent = parent
                async def __aenter__(self):
                    if not self.parent._mem_conn:
                         self.parent._mem_conn = await aiosqlite.connect(":memory:")
                    return self.parent._mem_conn
                async def __aexit__(self, *args):
                    # Do not close the connection for in-memory DB
                    pass 
            return NoCloseContext(self)
        else:
            return aiosqlite.connect(self.db_path)

    async def initialize(self) -> None:
        """
        Initialize the database schema.
        """
        async with self._db_context() as db:
            # Main Table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS main (
                    uuid char(40) PRIMARY KEY, 
                    added_time REAL NOT NULL CHECK (added_time > 0), 
                    last_used_time REAL CHECK (last_used_time > 0), 
                    mimetypes TEXT NOT NULL, 
                    text NTEXT, 
                    starred BOOLEAN
                );
            """)
            # Aux Table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS aux (
                    uuid char(40) NOT NULL, 
                    mimetype TEXT NOT NULL, 
                    data_uuid char(40) NOT NULL, 
                    PRIMARY KEY (uuid, mimetype)
                );
            """)
            # Version Table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS version (
                    db_version INT NOT NULL
                );
            """)
            
            # Check if version exists, if not insert default
            cursor = await db.execute("SELECT count(*) FROM version")
            count = (await cursor.fetchone())[0]
            if count == 0:
                 await db.execute("INSERT INTO version (db_version) VALUES (1)")
            
            await db.commit()

    async def _ensure_initialized(self) -> None:
        if not self._initialized:
            await self.initialize()
            self._initialized = True

    async def add(self, content: Content) -> None:
        """
        Adds a new entry to the history.
        """
        await self._ensure_initialized()

        async with self._db_context() as db:
            now = content.metadata.created_at.timestamp()
            await db.execute(
                """
                INSERT OR REPLACE INTO main (uuid, added_time, last_used_time, mimetypes, text, starred)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    str(content.metadata.id),
                    now,
                    now,
                    content.metadata.content_type,
                    content.data,
                    False # Default starred to False
                )
            )
            await db.commit()

    async def get_recent(self, limit: int = 10) -> List[Content]:
        """
        Retrieves recent history entries.
        """
        await self._ensure_initialized()

        async with self._db_context() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT uuid, added_time, mimetypes, text 
                FROM main 
                ORDER BY added_time DESC 
                LIMIT ?
                """,
                (limit,)
            )
            rows = await cursor.fetchall()
            
            results = []
            for row in rows:
                # Reconstruct Content object
                # Timestamp to datetime
                created_at = datetime.fromtimestamp(row['added_time'], tz=timezone.utc)
                
                content = Content(
                    data=row['text'] if row['text'] else "",
                    metadata=Metadata(
                        id=UUID(row['uuid']),
                        created_at=created_at,
                        content_type=row['mimetypes'],
                        source_app=None # Not stored in this schema
                    )
                )
                results.append(content)
            return results

    async def clear(self) -> None:
        """
        Clears the history storage.
        """
        await self._ensure_initialized()
        
        async with self._db_context() as db:
            await db.execute("DELETE FROM main")
            await db.execute("DELETE FROM aux")
            await db.commit()
