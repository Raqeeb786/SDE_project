from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from app.websocket.manager import ConnectionManager
from jose import jwt

manager= ConnectionManager()
router= APIRouter(prefix='/ws',tags=['Websocket'])

SECRET_KEY = "your-super-secret-key"
ALGORITHM = "HS256"

@router.websocket('/chat')
async def websocket_endpoint(
    websocket: WebSocket,
    token: str = Query(...)
):
    username = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
    await manager.connect(
    username,
    websocket
)
    await manager.broadcast_active_users()
    try:
        while True:
            message= await websocket.receive_text()
            if not message.strip():
                continue
            await manager.broadcast(username, message)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print('Client Disconnected')
        await manager.broadcast_active_users()
