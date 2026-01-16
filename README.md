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
