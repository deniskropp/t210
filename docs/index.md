# Klipper SDK Documentation

Welcome to the **Klipper SDK** documentation. This SDK provides a Pythonic interface for interacting with system clipboards (and potential future remote clipboards) through a unified, hexagonal architecture.

## Sections

### [API Reference](api/client.md)
Detailed reference for the `KlipperClient`, Domain Models, and Exceptions.

### [Architecture](architecture/overview.md)
Understand the core design, Hexagonal Architecture, and how the Service Layer orchestrates Adapters.

### [Guides](guides/configuration.md)
- [Configuration](guides/configuration.md)
- [Error Handling](guides/error_handling.md)
- [Development & Testing](guides/development.md)

## Quick Start

```python
import asyncio
from src.klipper_sdk.factory import create_client
from src.core.domain.models import Content

async def main():
    # Create a client (auto-selects best adapter)
    client = create_client()

    # Write to clipboard
    await client.set_content(Content.from_text("Hello Klipper!"))

    # Read from clipboard
    content = await client.get_content()
    print(content.data)

if __name__ == "__main__":
    asyncio.run(main())
```
