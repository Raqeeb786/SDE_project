import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [users, setUsers] = useState([]);
  const [username, setUsername] = useState("");

  const API_URL = "http://127.0.0.1:8000";

  async function fetchUsers() {
    const response = await fetch(`${API_URL}/users/`);
    const data = await response.json();

    setUsers(data);
  }

  async function createUser() {
    if (!username.trim()) return;

    const response = await fetch(`${API_URL}/users/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
      }),
    });

    const data = await response.json();

    console.log("Created:", data);

    setUsername("");

    // refresh list
    fetchUsers();
  }


  useEffect(() => {
    fetchUsers();
  }, []);


  return (
    <section id="center">

      <h1>Multiplayer Game</h1>

      <input
        type="text"
        placeholder="Enter username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <button onClick={createUser}>
        Create User
      </button>


      <h2>Players</h2>

      <ul>
        {
          users.map((user) => (
            <li key={user.id}>
              {user.id} - {user.username}
            </li>
          ))
        }
      </ul>

    </section>
  );
}

export default App;
