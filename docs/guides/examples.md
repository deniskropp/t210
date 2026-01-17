# Examples

## Basic Text Clipboard

```python
import asyncio
from src.klipper_sdk.factory import create_client
from src.core.domain.models import Content

async def main():
    client = create_client()
    
    # Write
    await client.set_content(Content.from_text("Important Data"))
    
    # Read
    content = await client.get_content()
    print(f"Clipboard contains: {content.data}")
    
    # History
    history = await client.get_recent()
    for item in history:
        print(f"History Item: {item.data} ({item.metadata.created_at})")

if __name__ == "__main__":
    asyncio.run(main())
```

## Custom Adapter

```python
from src.core.adapters.in_memory import InMemoryClipboardAdapter
from src.core.service.service import ClipboardService
from src.klipper_sdk.client.client import KlipperClient

# Manually assemble
adapter = InMemoryClipboardAdapter()
service = ClipboardService(adapter)
client = KlipperClient(service)
```
