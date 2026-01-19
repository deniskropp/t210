from typing import List, Any, Optional
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.console import RenderableType
from rich.syntax import Syntax

from src.core.domain.models import Content

class HistoryTable:
    """
    Renders the clipboard history as a table.
    """
    def __init__(self, title: str = "Clipboard History"):
        self.title = title

    def render(self, items: List[Content]) -> Table:
        table = Table(title=self.title, expand=True)

        # Columns as per spec: ID, Time, Type, Content Preview
        table.add_column("ID", style="dim cyan", no_wrap=True)
        table.add_column("Time", style="blue", no_wrap=True)
        table.add_column("Type", style="magenta")
        table.add_column("Content Preview", style="white")

        for item in items:
            # Format ID: Short UUID (first 8 chars)
            item_id = str(item.metadata.id)[:8]
            
            # Format Time: Relative (simulated or real)
            # Assuming timestamp is a datetime object in metadata
            time_str = item.metadata.created_at.strftime("%H:%M:%S") # Simplification for now, relative time logic can be added
            
            # Format Type
            content_type = item.metadata.content_type
            type_icon = "📝" if "text" in content_type else "📁"
            type_str = f"{type_icon} {content_type}"

            # Format Content Preview
            raw_content = item.data.decode("utf-8", errors="replace") if isinstance(item.data, bytes) else str(item.data)
            preview = raw_content[:50].replace("\n", "↵")
            
            table.add_row(item_id, time_str, type_str, preview)

        return table


class ItemDetail:
    """
    Renders detailed view of a single clipboard item.
    """
    def __init__(self, item: Content):
        self.item = item

    def render(self) -> Panel:
        # Layout: Header (Metadata), Body (Content), Footer (Actions)
        
        # Header
        item_id = str(self.item.metadata.id)
        timestamp = self.item.metadata.created_at.strftime("%Y-%m-%d %H:%M:%S")
        source = self.item.metadata.source_app or "Unknown"
        header_text = f"ID: [cyan]{item_id}[/cyan] | Time: [blue]{timestamp}[/blue] | Source: [green]{source}[/green]"

        # Body
        raw_content = self.item.data.decode("utf-8", errors="replace") if isinstance(self.item.data, bytes) else str(self.item.data)
        # Try highlighting if it looks like code, else plain text
        body_content = Syntax(raw_content, "python", theme="monokai", line_numbers=True) if "python" in self.item.metadata.content_type else raw_content

        # Footer
        footer_text = "[bold]Actions:[/bold] [yellow](c)[/yellow] Copy | [red](d)[/red] Delete | [blue](p)[/blue] Pin"

        # Combine into a Panel
        # For a simple Detail view, a Panel wrapping a Group or Text is sufficient. 
        # But to strictly separate Header/Body/Footer visually, existing Panel is good.
        
        content = Text.assemble(
            Text.from_markup(header_text),
            "\n\n",
            body_content if isinstance(body_content, Syntax) else Text(body_content),
            "\n\n",
            Text.from_markup(footer_text)
        )
        
        return Panel(content, title=f"Item Details: {self.item.metadata.content_type}", expand=True, border_style="cyan")


class ErrorPanel:
    """
    Renders an actionable error message.
    """
    def __init__(self, title: str, message: str, suggestion: Optional[str] = None):
        self.title = title
        self.message = message
        self.suggestion = suggestion

    def render(self) -> Panel:
        content = Text()
        content.append(f"{self.message}\n", style="bold red")
        if self.suggestion:
            content.append(f"\nSuggestion: {self.suggestion}", style="yellow italic")
            
        return Panel(content, title=f"Error: {self.title}", border_style="red", expand=True)
