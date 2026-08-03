from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from app.websocket.manager import ConnectionManager
from app.websocket.room_manager import room_manager
from app.websocket.events.schemas import WebSocketEvent
from app.websocket.events.router import event_router
from jose import jwt

manager= ConnectionManager()
router= APIRouter(prefix='/ws',tags=['Websocket'])

SECRET_KEY = "your-super-secret-key"
ALGORITHM = "HS256"

@router.websocket('/chat')
async def websocket_endpoint(
    websocket: WebSocket,
    token: str = Query(...),
    room_id: str = Query(...)
):
    username = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
    if not username:
        await websocket.close(code=1008)
        return
    # room_manager.join_room(room_id, username)
    if not room_manager.join_room(room_id, username):
        await websocket.close(code=1008)
        return
    await manager.connect(
    username,
    websocket
)
    # await manager.broadcast_active_users()
    await manager.broadcast_room_users(room_id)
    try:
        while True:
            data = await websocket.receive_json()
            print(f"Received data: {data}")
            event= WebSocketEvent(**data)
            print(f"Handling event: {event}")
            await event_router.handle(event , username ,room_id , manager)
            # message= await websocket.receive_text()
            # if not message.strip():
            #     continue
            # await manager.broadcast(
            #     room_id,
            #     username,
            #     message
            # )
    except WebSocketDisconnect:
        print('Client Disconnected')
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        room_manager.leave_room(room_id, username)
        manager.disconnect(websocket)
        # await manager.broadcast_active_users()
        await manager.broadcast_room_users(room_id)
