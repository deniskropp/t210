from datetime import datetime, timedelta, timezone
from rich.console import Console

from src.core.domain.models import Content, Metadata
from src.cli import HistoryTable, ItemDetail, MonitorStream

def main():
    console = Console()

    # Create dummy data
    now = datetime.now(timezone.utc)
    items = [
        Content(
            data="Hello world!",
            metadata=Metadata(
                created_at=now,
                content_type="text/plain",
                source_app="Terminal"
            )
        ),
        Content(
            data="def foo():\n    return 'bar'",
            metadata=Metadata(
                created_at=now - timedelta(minutes=5),
                content_type="text/x-python",
                source_app="VS Code"
            )
        ),
        Content(
            data='{"key": "value", "list": [1, 2, 3]}',
            metadata=Metadata(
                created_at=now - timedelta(days=1),
                content_type="application/json",
                source_app="Postman"
            )
        )
    ]

    # 1. Test HistoryTable
    console.rule("[bold cyan]Test: HistoryTable")
    history_table = HistoryTable()
    console.print(history_table.render(items))
    console.print()

    # 2. Test ItemDetail (Python code)
    console.rule("[bold cyan]Test: ItemDetail")
    detail = ItemDetail(items[1])
    console.print(detail.render())
    console.print()

    # 3. Test MonitorStream
    console.rule("[bold cyan]Test: MonitorStream")
    monitor = MonitorStream()
    console.print(monitor.format_event(now, "copy", "Text copied from 'Chrome' (15 chars)"))
    console.print(monitor.format_event(now, "sync", "Synced 1 item to cloud"))
    console.print(monitor.format_event(now, "error", "Connection failed"))
    console.print()

if __name__ == "__main__":
    main()
