import React, { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";

function Lobby(){

    const [room_id, setRoom_id] = useState("");
    const navigate = useNavigate();

    async function createRoom(){
        const response= await fetch(
            "https://opulent-space-spork-45rp7rjrpqw274gj-8000.app.github.dev/rooms/create",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                }
            }
        );
        if(!response.ok){
                console.error("Failed to create room");
                return;
            }
        const data = await response.json()
        console.log("Created room:", data.room_id);
        navigate(`/room/${data.room_id}`);
    }


    async function joinRoom(){
        const usernameResponse = await fetch(
            "https://opulent-space-spork-45rp7rjrpqw274gj-8000.app.github.dev/auth/me",
            {
                headers:{
                    "Authorization":
                    `Bearer ${sessionStorage.getItem("access_token")}`
                }
            }
        );
        const userData = await usernameResponse.json();
        const response = await fetch(
            "https://opulent-space-spork-45rp7rjrpqw274gj-8000.app.github.dev/rooms/join",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({
                    room_id: room_id,
                    username: userData.username
                })
            }
        );
        console.log(response)
        if (!response.ok){
            console.error("Room does not exist");
            return;
        }
        console.log(response)
        navigate(`/room/${room_id}`);
    }

        

    return(

    <div>
    <h1>CHOOSE GAMEPLAY</h1>

    <button onClick={createRoom}>Create Room</button>

    <br></br>
    <br></br>
    <input
            type="text"
            placeholder='Enter Room id'
            value={room_id}
            onChange={(e)=>setRoom_id(e.target.value)}
            />

            <button onClick={joinRoom}>Join Room</button>
            
    </div>
    )
}

export default Lobby