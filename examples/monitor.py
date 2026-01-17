import asyncio
from src.klipper_sdk.factory import create_client
from src.core.domain.models import Content
from src.core.domain.events import ClipboardEvent

async def event_handler(event: ClipboardEvent):
    print(f"Received Event: {event.type}")
    if event.data:
        print(f"  Data: {event.data.data}")

async def main():
    # Create the client (using InMemory adapter by default)
    client = create_client()

    print("Registering event listener...")
    observer = client.add_event_listener(event_handler)

    print("Simulating clipboard operations...")
    
    # 1. Set Content
    print("-> Setting content: 'Hello World'")
    await client.set_content(Content.from_text("Hello World", source_app="MonitorExample"))
    await asyncio.sleep(0.1) # Yield to let event loop process
    
    # 2. Set Content Again
    print("-> Setting content: 'Update'")
    await client.set_content(Content.from_text("Update", source_app="MonitorExample"))
    await asyncio.sleep(0.1)

    # 3. Clear
    print("-> Clearing clipboard")
    await client.clear()
    await asyncio.sleep(0.1)

    # Unsubscribe
    print("Unsubscribing...")
    client.remove_event_listener(observer)

    # 4. Set Content (Should not trigger)
    print("-> Setting content (should be silent)")
    await client.set_content(Content.from_text("Silent", source_app="MonitorExample"))
    await asyncio.sleep(0.1)
    
    print("Done.")

if __name__ == "__main__":
    asyncio.run(main())