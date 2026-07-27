import React, { useEffect, useRef, useState } from "react";

function HomePage(){
    const [username, setUsername] = useState("");
    const [message, setMessage] = useState("");
    const [messages, setMessages] = useState([]);
    const [onlineUsers, setOnlineUsers] = useState([]);
    const socketRef = useRef(null);

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
        const socket = new WebSocket(
        "wss://opulent-space-spork-45rp7rjrpqw274gj-8000.app.github.dev/ws/chat?token=" + sessionStorage.getItem("access_token")
        );

        socketRef.current = socket;

        socket.onopen = () => {
            console.log("Connected");
        };

        // socket.onmessage = (event) => {
        //     setMessages((prev) => [...prev, event.data]);
        // };

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            switch (data.type) {
                case "chat":
                    setMessages(prev => [...prev,data]);
                    break;
                case "user_list":
                    setOnlineUsers(data.users);
                    break;
            }
        };
                socket.onclose = () => {
            console.log("Disconnected");
        };

        return () => {
            socket.close();
        };
        }, []);

    return(
        <><h1>ARENA</h1>
        <h2>Welcome {username}</h2>

        <h3>Online Users</h3>
        <ul>
            {onlineUsers.map(user => (
                <li key={user}>
                    🟢 {user}
                </li>
            ))}

        </ul>

        <input 
            placeholder="Type your message..." 
            value={message}
            onChange={(e) => setMessage(e.target.value)}
        />
        <br></br>
        <button
            onClick={() => {
                if (
                    socketRef.current &&
                    socketRef.current.readyState === WebSocket.OPEN
                ) {
                    socketRef.current.send(message);
                    setMessage("");
                }
            }}
        >
            Send
        </button>

        <br />
        <div>
            {/* {messages.map((msg, index) => (
                <p key={index}>{msg}</p>
            ))} */}

            {messages.map((msg, index) => (
                <div key={index}>
                    <strong>{msg.sender}</strong>: {msg.message}
                </div>
            ))}
        </div>
        </>
    );
}

export default HomePage;