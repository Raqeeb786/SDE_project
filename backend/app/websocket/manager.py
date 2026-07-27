from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.websocket.model import ConnectedUser
import json


class ConnectionManager:
    def __init__(self):
        self.active_connections= {}

    async def send_json(self, websocket: WebSocket, data:dict):
        await websocket.send_text(json.dumps(data))
    
    def get_online_users(self):
        return list(self.active_connections.keys())
    
    async def connect(self, username: str, websocket: WebSocket):
        await websocket.accept()
        user = ConnectedUser(username=username, websocket=websocket)
        self.active_connections[username] = user
        
    def disconnect(self, websocket: WebSocket):
        disconnected_user = None

        for username, user in self.active_connections.items():
            if user.websocket == websocket:
                disconnected_user = username
                break
        if disconnected_user:
            del self.active_connections[disconnected_user]

    async def broadcast_active_users(self):
        payload = {
        "type": "user_list",
        "users": self.get_online_users()
        }
        for user in self.active_connections.values():
            await self.send_json(
                user.websocket,
                payload
            )



    async def broadcast(self, username: str, message: str):
        for user in self.active_connections.values():
            # await user.websocket.send_text(
            #     f"{username}: {message}"
            # )
            await self.send_json(user.websocket,{"type":"chat", "sender":username , "message":message})
            
    
