# Day 24 Notes

Took a look at the following sections from the Python3 app that Ricky found:
(https://apps.apple.com/us/app/learn-python-3-programming/id1489863294)

- Reg Expressions
- API Understanding
- numpy

- Networking
- Multithreading
- Python Webscraping
- Pandas and dataframes

PUT http://my.server/apples/{id}/color/{color}



Want to see when an item drops down to a specific price.
- Check 50 websites
    for each site in sites:
        check the price

synchronous:
    - kick off one and wait for it to finish before kicking off the next one.
asynchronous call:
    - start but do not wait

asyncwait
- Continue after all threads are finished.

RAID 5/10:
Over 4 disks fith one is called a parity

xxxxxxxxxxxxxx
xxxxxxxxxxxxxx
xxxxxxxxxxxxxx

## API

Methods (Actions):
- GET - One or Get all
- PUT - Updating One or more
- DELETE - Deleting one or more
- POST - Create one

# Multi-Player Game
Resources:
- /players
    - username [REQUIRED] <String> : No spaces, require a number
    - password [REQUIRED] <String> : One capital, 8 chars, One lower, a number, a special character
    - displayName [REQUIRED] <String> : No profanity
    - cumulativeScore [OPTIONAL] <Integer> : Default 0, may need to restrict how you are able to update
    - level [OPTIONAL] <String> : Default Beginner : Enum[Beginner, Novice, Intermediate, Advanced, BadAss]
    - gameId [OPTIONAL] <String> : uuid : default None
    - state = [OPTIONAL] <String> : ENUM [IN_LOBBY, IN_GAME, OFFLINE] : Default OFFLINE
    - avatar = [OPTIONAL] <url> : Default None

    - ACTIONS
        - GET /players
            - Will return all players in the database
            - return HTTP 200 (Success)
        - POST /players
            - Create a player
            - return HTTP 201 (Created)
        - PUT /players/{username}
            {
                "rating": 5,
                "state": "IN_GAME"
            }
    - Files in source control
        - controller/players.py
            - Create a class PlayersCollection for actions agains the plural endpoint /players
                - GET /players: returning more than one player
                    - service/players.py::get_all()
                - POST /players: create player
                    - service/players.py::create_one()
            - Create a class Player for actions agains a individual /players/{id}
                - GET /players/{id}
                - PUT /players/{id}
                - DELETE /players/{id}
            GET, POST, PUT, DELETE
        - create a players namespace
            - Create a class PlayerHistory /players/{id}/history
                - GET : return history of all games played
                    - service/players.py:get_history(id)
                        - service/active-log-entries.py::get_by_username(id)
- /games
    - gameId
    - players [
        'playerOneUsername',
        'playerTwoUsername'
    ]

- /activity-log-entries
    - gameId
    - winner
    - duration
    - players []
        - username
        - rating
    - loser
    - startDateTime

    ACTIONS:
        - /activity-log-entries/{id}: returns all entries for a specific player {id}



Others:
- ranking
- namespaces
- lobby

/resource/{resourceId}/{resource}

PUT /games/{gameId}/players/{username}
GET /games/{gameId}/players
DELETE /games/{gameId}/players/{username}

<schema/model validation>
controller/players.py:
    - service/players.py::create_one(payload)
        - <schema/model validation>
    
<schema/model validation>
controller/games.py:
    - service/games.py::create_one(payload)
        - <schema/model validation>

    service/handle_game_timeouts.py::kick_player_out_of_game():
        service/games.py::delete_player_from_game(gameId, username)
 

## Homework
Build out the API for players and the services to make it work