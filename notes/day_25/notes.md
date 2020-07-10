# Day 25

## Things to talk about

Took a look at the following sections from the Python3 app that Ricky found:
(https://apps.apple.com/us/app/learn-python-3-programming/id1489863294)

- Reg Expressions
- API Understanding  -- DONE
- numpy

- Networking
- Multithreading
- Python Webscraping
- Pandas and dataframes

Example of what a rest endpoint may look like that will update the color for a apple resource
PUT http://my.server/apples/{id}/color/{color}
- Resources should be plural (ex: the resource iin the above url is apples)


PUT http://my.server.com/players/{username}
{
    "password": "ABC123",
    "status": "IN_LOBBY"
}

PUT http://my.server.com/players/{username}/status/{offline}



## numpy

a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,6,7,8,9]
c = a * b
