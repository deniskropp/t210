from contextlib import asynccontextmanager
from typing import Optional
from rich.console import Console
from rich.status import Status

class AsyncFeedback:
    """
    Handles user feedback for asynchronous operations.
    """
    def __init__(self, console: Optional[Console] = None):
        self.console = console or Console()

    @asynccontextmanager
    async def spinner(self, message: str, success_message: Optional[str] = "Done!"):
        """
        Async context manager for showing a spinner during long operations.
        """
        status = self.console.status(message, spinner="dots")
        status.start()
        try:
            yield status
        finally:
            status.stop()
            if success_message:
                self.console.print(f"[green]✔[/green] {success_message}")

    def notify(self, message: str, level: str = "info"):
        """
        Simple notification.
        """
        style = "bold white"
        if level == "success":
            style = "bold green"
        elif level == "error":
            style = "bold red"
        elif level == "warning":
            style = "bold yellow"
            
        self.console.print(f"[{style}]{message}[/{style}]")
