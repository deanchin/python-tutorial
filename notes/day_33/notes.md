# Day 33 Notes

Response Code = number: 200, 404, 201
Response Body = {
    "message": "gotem"
}

alert the next player that it is their turn: return who the next player.

scenarios:
* valid move --> HTTP 200
* invalid move --> HTTP 403

# HTTP 200 - valid move showDetails=true/false
{
    "message": "Move recorded, moving to next player",
    "board": [board],
    "playerUp": "Yellow"
}

# HTTP 403 - invalid move
{
    "message": "Column {col_no} is full"
}

# HTTP 403 - invalid move
{
    "message": "Column {col_no} is not on the board"
}

# HTTP 403 - invalid move
{
    "message": "It's not your turn bro"
}


2 lists

list1 - l1-1,l1-2,l1-3,l1-4
list2 - l2-1,l2-2,l2-3,l2-4

currL1 = l1-3
currL2 = l2-2

compare currL1 to currL2.

whoever is smaller, add it to list3
- next on the smaller