import { useState } from "react";
import {useNavigate} from 'react-router-dom';

function LoginPage() {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const navigate= useNavigate();

    async function register(){
        const response = await fetch("https://opulent-space-spork-45rp7rjrpqw274gj-8000.app.github.dev/auth/register",
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
        // const response= await fetch("http://localhost:8000/auth/login",
        const response= await fetch("https://opulent-space-spork-45rp7rjrpqw274gj-8000.app.github.dev/auth/login",
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
        if (!response.ok) {
            console.error("Login failed:", response.statusText);
            return;
        }
        const data = await response.json();
        sessionStorage.setItem("access_token" , data.access_token);
        navigate('/home');
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
