import { useState } from "react";

function LoginPage() {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    async function register(){
        const response = await fetch("http://localhost:8000/users/",
            {
                method:'POST',
                headers:{
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            });
        const data = await response.json();
        console.log("Created:", data);
    }

    async function login(){
        const response= await fetch("http://localhost:8000/users/login",
            {
                method:'POST',
                headers:{
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            });
        const data = await response.json();
        console.log("Logged in:", data);
    }

    return (
        <div>

            <h1>Multiplayer Game</h1>

            <input
                type="text"
                placeholder="Enter username"
                value={username}
                onChange={(e)=>setUsername(e.target.value)}
            />
            <input
            type="password"
            placeholder='Enter Password'
            value={password}
            onChange={(e)=>setPassword(e.target.value)}
            />

            <button onClick={register}>Register</button>
            <button onClick={login}>login</button>



        </div>
    );
}

export default LoginPage;
