from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from app.websocket.manager import ConnectionManager
from app.websocket.room_manager import room_manager
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
            message= await websocket.receive_text()
            if not message.strip():
                continue
            await manager.broadcast(
                room_id,
                username,
                message
            )
    except WebSocketDisconnect:
        room_manager.leave_room(room_id, username)
        manager.disconnect(websocket)
        print('Client Disconnected')
        # await manager.broadcast_active_users()
        await manager.broadcast_room_users(room_id)
