import sys
from typing import Optional

from src.core.adapters.in_memory import InMemoryClipboardAdapter
from src.core.adapters.sqlite_storage import SQLiteStorage
from src.core.service.service import ClipboardService
from src.klipper_sdk.client.client import KlipperClient

def create_client(adapter: str = "auto") -> KlipperClient:
    """
    Factory to create a KlipperClient instance.

    Args:
        adapter: The adapter strategy to use. 
                 Options: 'auto' (default), 'in_memory'.
                 'auto' generally attempts to treat platform specific first, falling back to in_memory.
    """
    
    clipboard_adapter_instance = None
    history_adapter_instance = None
    
    if adapter == "auto":
        # Strategy: Use SQLite for history by default in auto mode
        history_adapter_instance = SQLiteStorage()
        
        if sys.platform == "linux":
            try:
                from src.core.adapters.linux import LinuxClipboardAdapter
                clipboard_adapter_instance = LinuxClipboardAdapter()
            except ImportError:
                # Log warning: No system clipboard tool found, falling back.
                pass
            except Exception:
                pass
    
    # Fallback or explicit in_memory
    if adapter == "in_memory" or clipboard_adapter_instance is None:
        clipboard_adapter_instance = InMemoryClipboardAdapter()
        
        # If explicit in_memory, use memory DB
        if adapter == "in_memory":
             history_adapter_instance = SQLiteStorage(db_path=":memory:")
        # If auto fallback, we stick with what we have (or create memory DB if None)
        elif history_adapter_instance is None: 
             history_adapter_instance = SQLiteStorage(db_path=":memory:")

    # Ensure we have both
    if clipboard_adapter_instance is None:
        clipboard_adapter_instance = InMemoryClipboardAdapter()
    if history_adapter_instance is None:
        history_adapter_instance = SQLiteStorage(db_path=":memory:")

    service = ClipboardService(
        clipboard_adapter=clipboard_adapter_instance,
        history_adapter=history_adapter_instance
    )
    return KlipperClient(service=service)