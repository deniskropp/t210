from datetime import datetime, timezone
from typing import List

from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.syntax import Syntax
from rich.console import RenderableType

from src.core.domain.models import Content

def _format_relative_time(dt: datetime) -> str:
    now = datetime.now(timezone.utc)
    diff = now - dt
    
    seconds = diff.total_seconds()
    if seconds < 60:
        return "Just now"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} min{'s' if minutes > 1 else ''} ago"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    else:
        days = int(seconds / 86400)
        return f"{days} day{'s' if days > 1 else ''} ago"

class HistoryTable:
    def __init__(self, title: str = "Clipboard History"):
        self.title = title

    def render(self, items: List[Content]) -> Table:
        table = Table(title=self.title, expand=True)
        
        table.add_column("ID", style="dim cyan", no_wrap=True)
        table.add_column("Time", style="blue")
        table.add_column("Type", style="magenta")
        table.add_column("Content Preview", style="white")

        for item in items:
            preview = item.data[:50].replace("\n", "↵")
            if len(item.data) > 50:
                preview += "..."
                
            type_icon = "📝 " if "text" in item.metadata.content_type else "📦 "
            type_display = f"{type_icon}{item.metadata.content_type}"
            
            table.add_row(
                str(item.metadata.id)[:8],
                _format_relative_time(item.metadata.created_at),
                type_display,
                preview
            )
            
        return table

class ItemDetail:
    def __init__(self, item: Content):
        self.item = item

    def render(self) -> Panel:
        # Header
        meta = self.item.metadata
        header = f"[bold cyan]ID:[/bold cyan] {meta.id} | [bold blue]Time:[/bold blue] {meta.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}"
        if meta.source_app:
            header += f" | [bold magenta]Source:[/bold magenta] {meta.source_app}"

        # Body
        if "text" in meta.content_type or "json" in meta.content_type:
             # Basic syntax highlighting guess
             lexer = "json" if "json" in meta.content_type else "text"
             body = Syntax(self.item.data, lexer, theme="monokai", word_wrap=True)
        else:
            body = Text(self.item.data)

        # Footer
        footer = "[dim]Actions: [bold white]c[/bold white]opy | [bold white]d[/bold white]elete | [bold white]p[/bold white]in[/dim]"

        return Panel(
            body,
            title=header,
            subtitle=footer,
            expand=True,
            border_style="cyan"
        )
