import asyncio
import uuid
from datetime import datetime
from rich.console import Console
from rich.panel import Panel

from src.core.domain.models import Content, Metadata
from src.cli.components import HistoryTable, ItemDetail
from src.cli.feedback import AsyncFeedback
from src.cli.monitor import MonitorStream

async def run_demo():
    console = Console()
    console.clear()
    console.rule("[bold cyan]Klipper SDK UI/UX Demo[/bold cyan]")

    # 1. Feedback Demo
    feedback = AsyncFeedback(console)
    async with feedback.spinner("Simulating loading clipboard history..."):
        await asyncio.sleep(1.0) # Simulate work

    # 2. History Table Demo
    console.print("\n[bold]1. History Table Component[/bold]")
    
    # Create dummy data
    dummy_items = [
        Content(
            data="Hello Klipper!",
            metadata=Metadata(id=uuid.UUID("12345678-1234-5678-1234-567812345678"), created_at=datetime.now(), content_type="text/plain", source_app="Terminal")
        ),
        Content(
            data="https://example.com",
            metadata=Metadata(id=uuid.UUID("abcdef09-1234-5678-1234-567812345678"), created_at=datetime.now(), content_type="text/plain", source_app="Firefox")
        ),
        Content(
            data="<binary image placeholder>",
            metadata=Metadata(id=uuid.UUID("7890abcd-1234-5678-1234-567812345678"), created_at=datetime.now(), content_type="image/png", source_app="GIMP")
        ),
    ]

    history_table = HistoryTable()
    console.print(history_table.render(dummy_items))

    # 3. Item Detail Demo
    console.print("\n[bold]2. Item Detail Component[/bold]")
    
    detail_item = dummy_items[0]
    item_detail = ItemDetail(detail_item)
    console.print(item_detail.render())

    # 4. Monitor Stream Demo
    console.print("\n[bold]3. Monitor Stream Component (Simulation)[/bold]")
    monitor = MonitorStream()
    
    events = [
        (datetime.now(), "COPY", "Text copied from 'Chrome' (150 chars)"),
        (datetime.now(), "SYNC", "Synced 1 item to cloud"),
        (datetime.now(), "ERROR", "Failed to connect to daemon"),
    ]
    
    for ts, type_, details in events:
        console.print(monitor.format_event(ts, type_, details))

    console.rule("[bold cyan]Demo Complete[/bold cyan]")

if __name__ == "__main__":
    asyncio.run(run_demo())
