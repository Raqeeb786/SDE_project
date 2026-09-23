function OnlineUsers({ onlineUsers}) {
    return(
        <>
        <h3>Online Users</h3>
        <ul>
            {onlineUsers.map(user => (
                <li key={user}>
                    🟢 {user}
                </li>
            ))}
        </ul>
        </>
    )
}

