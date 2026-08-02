import random
import string


class RoomManager():
    def __init__(self):
        self.rooms={}

    def room_exists(self, room_id):
        return room_id in self.rooms

    def get_room(self, room_id):
        return self.rooms.get(room_id)
    
    def get_players(self, room_id):
        room = self.get_room(room_id)
        if room is None:
            return set()
        return room["players"]

    def get_host(self, room_id):
        room = self.get_room(room_id)
        if room is None:
            return None
        return room["host"]

    def get_status(self, room_id):
        room = self.get_room(room_id)
        if room is None:
            return None
        return room["status"]

    def get_room_info(self, room_id):
        room = self.get_room(room_id)
        if room is None:
            return None
        return {
            "room_id": room_id,
            "host": room["host"],
            "players": list(room["players"]),
            "status": room["status"]
        }

    def generate_room_id(self):
        chars = string.ascii_uppercase + string.digits
        return ''.join(
            random.choice(chars)
            for _ in range(6)
        )

    def create_room(self):
        while True:
            room_id = self.generate_room_id()
            if room_id not in self.rooms:
                self.rooms[room_id] = {
                    "host": None,
                    "players": set(),
                    "status": "waiting"
                }
                return room_id

    def join_room(self, room_id , username):
        if room_id not in self.rooms:
            return False
        self.rooms[room_id]["players"].add(username)
        return True
            

    def leave_room(self, room_id, username):
        if room_id in self.rooms:
            self.rooms[room_id]["players"].discard(username)
            if len(self.rooms[room_id]["players"]) == 0:
                del self.rooms[room_id]

    def get_rooms(self):
        return list(self.rooms.items())
        
room_manager= RoomManager()

