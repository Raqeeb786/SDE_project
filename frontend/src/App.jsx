// import { useEffect, useState } from "react";
// import "./App.css";

// function App() {
//   const [users, setUsers] = useState([]);
//   const [username, setUsername] = useState("");
//   const [password, setPassword]= useState("");

//   const API_URL = "http://127.0.0.1:8000";

//   async function fetchUsers() {
//     const response = await fetch(`${API_URL}/users/`);
//     const data = await response.json();

//     setUsers(data);
//   }

//   async function createUser() {
//     if (!username.trim()) return;
//     if (!password.trim()) return (alert('Password cant be empty!'));

//     const response = await fetch(`${API_URL}/users/`, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({
//         username: username,
//         password: password,
//       }),
//     });

//     const data = await response.json();

//     console.log("Created:", data);

//     setUsername("");

//     // refresh list
//     fetchUsers();
//   }


//   useEffect(() => {
//     fetchUsers();
//   }, []);


//   return (
//     <section id="center">

//       <h1>Multiplayer Game</h1>

//       <input
//         type="text"
//         placeholder="Enter username"
//         value={username}
//         onChange={(e) => setUsername(e.target.value)}
//       />

//       <input
//         type="password"
//         placeholder="Enter Password"
//         value={password}
//         onChange={(e) => setPassword(e.target.value)}
//         />
        
//       <button onClick={createUser}>
//         Create User
//       </button>


//       <h2>Players</h2>

//       <ul>
//         {
//           users.map((user) => (
//             <li key={user.id}>
//               {user.id} - {user.username}
//             </li>
//           ))
//         }
//       </ul>

//       <br>
//       </br>

//       <button>clcik me not</button>
//       <ul>
//         {
//           users.map((user) => (
//             <li key={user.id}>
//               {user.id} - {user.password}
//             </li>
//           ))
//         }
//       </ul>


//     </section>
//   );
// }

// export default App;





import { BrowserRouter, Routes, Route } from "react-router-dom";

import LoginPage from "./pages/loginPage";
import HomePage from "./pages/homePage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/home" element={<HomePage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
