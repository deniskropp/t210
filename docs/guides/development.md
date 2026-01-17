# Development & Testing Guide

## Running Tests

We use `pytest` for all testing.

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest -v tests/
```

## Adding Adapters

To add a new clipboard backend:
1.  Create a new file in `src/core/adapters/` (e.g., `my_os.py`).
2.  Implement the `ClipboardPort` interface.
3.  Update the `ClientFactory` (or manually inject it).

## Formatting

We follow standard Python PEP8. Please use `ruff` or `black` before submitting changes.
