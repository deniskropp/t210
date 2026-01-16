import asyncio
from klipper_sdk.client.client import KlipperClient
from klipper_sdk.core.models import ClipboardContent

async def main():
    print("Initializing Client...")
    client = KlipperClient()

    # Set content
    print("Setting content...")
    content = ClipboardContent(data="Hello Klipper Example!", mime_type="text/plain")
    await client.set_content(content)
    print("Content set!")

    # Retrieve content
    print("Getting content...")
    fetched = await client.get_content()
    print(f"Retrieved: {fetched.data} (Mime: {fetched.mime_type})")

    # Clear content
    print("Clearing content...")
    await client.clear()
    cleared = await client.get_content()
    print(f"Content after clear: '{cleared.data}'")

if __name__ == "__main__":
    asyncio.run(main())
