from datetime import datetime
from rich.text import Text
from rich.console import RenderableType

class MonitorStream:
    def format_event(self, timestamp: datetime, event_type: str, details: str) -> RenderableType:
        """
        Formats a single event line for the monitor stream.
        Format: [Timestamp] [Event Type] Details
        """
        time_str = timestamp.strftime("%H:%M:%S")
        
        # Color coding for event types
        type_style = "bold white"
        if event_type.upper() == "COPY":
            type_style = "bold green"
        elif event_type.upper() == "ERROR":
            type_style = "bold red"
        elif event_type.upper() == "SYNC":
            type_style = "bold blue"

        text = Text()
        text.append(f"[{time_str}] ", style="dim white")
        text.append(f"[{event_type.upper()}] ", style=type_style)
        text.append(details)
        
        return text
