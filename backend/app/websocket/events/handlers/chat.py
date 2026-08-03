from app.websocket.manager import ConnectionManager

class ChatHandler:

    async def handle(
        self,
        event,
        username,
        room_id,
        manager
    ):

        message = event.payload.get("message")

        if not message:
            return

        await manager.broadcast(
            room_id,
            username,
            message
        )


chat_handler = ChatHandler()