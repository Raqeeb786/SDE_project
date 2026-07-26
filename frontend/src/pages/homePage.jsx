import { useEffect } from "react";
import React , {useState} from 'react';

function homePage(){
    const [username, setUsername] = useState("");
    const [message, setMessage] = useState("");
    const [messages, setMessages] = useState([]);

    async function getUsername(){
        const token = sessionStorage.getItem("access_token");
        // console.log("Token:", token);
        const response = await fetch("https://opulent-space-spork-45rp7rjrpqw274gj-8000.app.github.dev/auth/me",{
            method:'GET',
            headers:{
                "content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            }
        });
        // console.log("Response status:", response.status);
        if (!response.ok) {
            console.error("Failed to fetch username:", response.statusText);
            return;
        }
        const data = await response.json();
        setUsername(data.username);
    }

    useEffect(() => {
        getUsername();
    }, []);

    return(
        <><h1>ARENA</h1>
        <h2>Welcome {username}</h2>

        <input 
            placeholder="Type your message..." 
            value={message}
            onChange={(e) => setMessage(e.target.value)}
        />
        <br></br>
        <button onClick={() => {
            setMessages([...messages, message]);
            setMessage("");
        }}>Send</button>

        <br />
        <div>
            {messages.map((msg, index) => (
                <p key={index}>{username}: {msg}</p>
            ))}
        </div>
        </>
    );
}

export default homePage;