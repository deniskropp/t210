import sys
from src.core.adapters.in_memory import InMemoryClipboardAdapter
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
    
    adapter_instance = None
    
    if adapter == "auto":
        if sys.platform == "linux":
            try:
                from src.core.adapters.linux import LinuxClipboardAdapter
                adapter_instance = LinuxClipboardAdapter()
            except ImportError:
                # Log warning: No system clipboard tool found, falling back.
                pass
            except Exception:
                pass
    
    if adapter_instance is None:
        adapter_instance = InMemoryClipboardAdapter()

    service = ClipboardService(adapter=adapter_instance)
    return KlipperClient(service=service)
