from app.websocket.events.handlers.chat import chat_handler


class EventRouter:

    def __init__(self):

        self.handlers = {
            "chat": chat_handler
        }


    async def handle(
        self,
        event,
        username,
        room_id,
        manager
    ):

        handler = self.handlers.get(event.type)

        if handler:
            await handler.handle(
                event,
                username,
                room_id,
                manager
            )

event_router = EventRouter()