# Welcome to Klipper SDK

A comprehensive, modern Python SDK for the Klipper clipboard manager.

## Overview

The Klipper SDK provides a robust, asynchronous interface for interacting with the Klipper clipboard manager. It is designed with modern Python practices in mind, featuring full type hinting, Pydantic v2 models, and an asyncio-first approach.

## Key Features

- **Asynchronous API**: Built on `asyncio` for non-blocking operations.
- **Type Safety**: Fully typed codebase utilizing strict MyPy settings.
- **Modern Data Models**: Uses Pydantic v2 for validation and serialization.
- **Rich CLI Support**: Integrated with `rich` for beautiful terminal output.

## Installation

```bash
pip install klipper-sdk
```

## Quick Start

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

if __name__ == "__main__":
    asyncio.run(main())
```
