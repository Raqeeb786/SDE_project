from fastapi import APIRouter, Depends, HTTPException
from app.websocket.room_manager import room_manager
from pydantic import BaseModel

class JoinRoomRequest(BaseModel):
    room_id: str
    username: str

router = APIRouter(prefix="/rooms", tags=["Room management"])

@router.post("/create")
def create_room():
    room_id = room_manager.create_room()
    if room_id:
        return {
            "message": "room successfully created",
            "room_id": room_id,
        }
    raise HTTPException(status_code=500, detail="Room creation failed")

# @router.post("/join")
# def join_room(room_id:str, username:str):
#     if room_manager.join_room(room_id, username):
#         return {
#             "message": "Joined room",
#             "room_id": room_id
#         }
#     else:
#         return{
#             "message": "room doesnt exist",
#         }


@router.post("/join")
def join_room(data: JoinRoomRequest):
    if room_manager.join_room(data.room_id, data.username):
        return {
            "message": "Joined room",
            "room_id": data.room_id
        }

    return {
        "message": "room doesnt exist"
    }

@router.get("/get")
def show():
    return {"rooms": room_manager.get_rooms(),
    }

@router.get("/{room_id}")
def get_room(room_id: str):
    room = room_manager.get_room_info(room_id)
    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )
    return room