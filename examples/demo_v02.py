import asyncio
from src.core.domain.models import Content
from src.core.adapters.in_memory import InMemoryClipboardAdapter
from src.shared.logging_config import logger

async def main():
    logger.info("Starting Klipper SDK v0.2.0 Demo (Core Foundation)...")

    # 1. Initialize Adapter
    adapter = InMemoryClipboardAdapter()
    
    # 2. Create Content
    content = Content.from_text("Hello Klipper v0.2.0!", source_app="DemoScript")
    logger.info(f"Created Content: {content.data} (Source: {content.metadata.source_app})")

    # 3. Write to Clipboard
    await adapter.write(content)
    logger.info("Content written to InMemoryAdapter.")

    # 4. Read back
    read_content = await adapter.read()
    if read_content:
        logger.info(f"Read Content: {read_content.data}")
        assert read_content.data == "Hello Klipper v0.2.0!"
    else:
        logger.error("Failed to read content!")

    # 5. Check History
    history = await adapter.history()
    logger.info(f"History Count: {len(history)}")

    logger.info("Demo Completed Successfully.")

if __name__ == "__main__":
    asyncio.run(main())
