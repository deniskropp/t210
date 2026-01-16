import asyncio
from klipper_sdk.client.client import KlipperClient
from klipper_sdk.core.models import ClipboardContent

async def main():
    client = KlipperClient()

    # Add some history
    print("Populating history...")
    for i in range(5):
        await client.set_content(ClipboardContent(data=f"Item {i}", mime_type="text/plain"))

    # Get recent
    print("Fetching recent items...")
    recent = await client.get_recent(limit=3)
    for item in recent:
        print(f" - {item.content.data} (ID: {item.id})")

    # Clear history
    print("Clearing history...")
    await client.clear_history()
    recent_after = await client.get_recent()
    print(f"History count after clear: {len(recent_after)}")

if __name__ == "__main__":
    asyncio.run(main())
