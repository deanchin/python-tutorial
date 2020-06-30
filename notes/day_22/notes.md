# Day 22 Notes

# How would you m,ake the Tic Tac Toe game online?




6 users:
- Connect users
- User will need access and have to log in so you know who they are
- Need to create an id / register if they are a new user.
- Create an invite.

- Lobby
- Choice of starting your own game or joining someone else's game
- If they create a game, they can invite someone to play.
    - Invitation / notification sent to other user


```bash
# User document
{
    "username": "dean",
    "password": "Password123",
    "emailAddress": "dean@gmail.com",
    "avatar": "url", <-- or maybe save this or upload
    "gameStatistics": {
        "wins": 34,
        "losses": 12,
        "tied": 2
    },
    "level": 4,
    "gameLog": {

    },
    "friends": ["billy", "bob", "johnny"],
    "activeGameId": 1
}

# Games
{
    "game_id": 1,
    "board": [[X,2,3],[O,5,6],[7,8,9]],
    "lastActivity": "date/time stamp",

}

# Activity Log
{
    "gameHistory": [
        {
            "datePlayed": "date/time stamp".
            "players": [
                {
                    "username": "dean",
                    "level": 3
                },
                {
                    "username": "samuel",
                    "level": 5
                }
            ],
            "winner": "samuel",
            "active": True/False
        }
    ]
}
```

