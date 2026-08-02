from fastapi import WebSocket
from app.websocket.model import ConnectedUser
from app.websocket.room_manager import room_manager
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

    async def broadcast_room_users(self, room_id: str):
        players = room_manager.get_players(room_id)
        payload = {
            "type": "user_list",
            "users": list(players)
        }
        for username in players:
            user = self.active_connections.get(username)
            if user:
                await self.send_json(user.websocket, payload)



    async def broadcast(self, room_id: str, username: str, message: str):
        # users_in_room = room_manager.rooms.get(room_id, set())
        users_in_room = room_manager.get_players(room_id)
        for username_in_room in users_in_room:
            user = self.active_connections.get(username_in_room)
            if user:
                await self.send_json(
                    user.websocket,
                    {
                        "type": "chat",
                        "sender": username,
                        "message": message
                    }
                )
            
    
