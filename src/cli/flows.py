import asyncio
from typing import List, Optional
from rich.console import Console
from rich.prompt import Prompt

from src.core.domain.models import Content
from src.cli.components import HistoryTable
from src.cli.feedback import AsyncFeedback

class CLIWorkflows:
    """
    Implements interaction flows defined in the UI/UX spec.
    """
    def __init__(self, console: Optional[Console] = None):
        self.console = console or Console()
        self.feedback = AsyncFeedback(self.console)

    async def search_history_flow(self, query: str, search_func):
        """
        Flow for searching clipboard history.
        """
        async with self.feedback.spinner(f"Searching for [italic]'{query}'[/italic]...", success_message=None):
            # Simulate or execute search
            results = await search_func(query)
            
        if not results:
            self.console.print(f"[yellow]No items found matching '{query}'[/yellow]")
            return

        history_table = HistoryTable(title=f"Search Results for '{query}'")
        self.console.print(history_table.render(results))

    async def interactive_selection_flow(self, items: List[Content], on_select):
        """
        Flow for interactive item selection.
        Since we are in a text-based SDK, we simulate interactive selection
        or use a simple prompt for ID selection as a placeholder for fully interactive UI.
        """
        if not items:
            self.console.print("[yellow]No items to select.[/yellow]")
            return

        history_table = HistoryTable(title="Select an item")
        self.console.print(history_table.render(items))
        
        choices = [str(item.metadata.id)[:8] for item in items]
        selected_id_short = Prompt.ask("Enter short ID to select", choices=choices)
        
        selected_item = next(i for i in items if str(i.metadata.id).startswith(selected_id_short))
        
        await on_select(selected_item)
        self.feedback.notify(f"Selected item {selected_id_short} copied to clipboard!")
