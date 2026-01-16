import asyncio
from klipper_sdk.client.client import KlipperClient
from klipper_sdk.core.models import ClipboardContent

async def monitor_clipboard(client: KlipperClient):
    print("Starting monitor...")
    async for item in client.monitor():
        print(f"Monitor received: {item.data}")

async def main():
    client = KlipperClient()

    # Start monitor in background
    monitor_task = asyncio.create_task(monitor_clipboard(client))

    # Give monitor a moment to start
    await asyncio.sleep(0.1)

    # Simulate changes
    print("Simulating clipboard changes...")
    await client.set_content(ClipboardContent(data="Change 1", mime_type="text/plain"))
    await asyncio.sleep(0.1)
    
    await client.set_content(ClipboardContent(data="Change 2", mime_type="text/plain"))
    await asyncio.sleep(0.1)

    # Cancel monitor
    print("Stopping monitor...")
    monitor_task.cancel()
    try:
        await monitor_task
    except asyncio.CancelledError:
        print("Monitor stopped.")

if __name__ == "__main__":
    asyncio.run(main())
