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
    
    # Simple logic for now: default to InMemory if auto or explicit
    # Later we will add:
    # if adapter == "auto":
    #    try_platform_adapters()...
    
    adapter_instance = InMemoryClipboardAdapter()
    service = ClipboardService(adapter=adapter_instance)
    return KlipperClient(service=service)
