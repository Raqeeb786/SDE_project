import asyncio
import websockets


async def test_websocket():
    uri = "ws://localhost:8000/ws/chat"

    async with websockets.connect(uri) as websocket:
        print("Connected")

        messages = [
            "Hello",
            "How are you?",
            "Testing multiple messages"
        ]

        for msg in messages:
            await websocket.send(msg)

            response = await websocket.recv()

            print("Sent:", msg)
            print("Received:", response)


asyncio.run(test_websocket())