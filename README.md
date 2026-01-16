# Klipper SDK

A comprehensive, modern Python SDK for the Klipper clipboard manager.

## Overview

The Klipper SDK provides a robust, asynchronous interface for interacting with the Klipper clipboard manager. It is designed with modern Python practices in mind, featuring full type hinting, Pydantic v2 models, and an asyncio-first approach.

## Features

- **Asynchronous API**: Built on `asyncio` for non-blocking operations.
- **Type Safety**: Fully typed codebase utilizing strict MyPy settings.
- **Modern Data Models**: Uses Pydantic v2 for validation and serialization.
- **Rich CLI Support**: Integrated with `rich` for beautiful terminal output.

## Installation

```bash
pip install klipper-sdk
```

## Quick Start

Here is a simple example of how to use the `KlipperClient` to set and retrieve clipboard content:

```python
import asyncio
from klipper_sdk.client.client import KlipperClient
from klipper_sdk.core.models import ClipboardContent

async def main():
    client = KlipperClient()

    # Set content
    content = ClipboardContent(data="Hello Klipper!", mime_type="text/plain")
    await client.set_content(content)
    print("Content set!")

    # Retrieve content
    fetched = await client.get_content()
    print(f"Retrieved: {fetched.data}")

    # Monitor changes
    print("Monitoring (press Ctrl+C to stop)...")
    async for item in client.monitor():
        print(f"Clipboard changed: {item.data}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Development

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -e ".[test,lint]"
   ```
3. Run tests:
   ```bash
   pytest
   ```