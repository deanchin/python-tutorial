# Day 21 Notes

## Things to cover

* Look at Ricky's code and help debug issue with controller.
* Take a look at pseudo code for tic-tac-toe.

## Tic Tac Toe Discussion

- Board layout [3x3]
- We need to be able to print it
- Need to be able to store information in each cell/position
- Need to be able to reset it
- Need to have a way to track whose turn it is
- Need to be able to have an easy way for thee user to select the position

- Need to have a way to figure out if there is a winner after each turn.

```bash
# Play 0
1   2   3
4   5   6
7   8   9

# Play 1    # --> active_player = X, prompt position, is position occupied, place player choice in array
x   2   3   # --> check for win, end game if winner
4   5   6   # --> check if all positions occupied, end game if stalemate
7   8   9

# Play 2
x   2   3   # --> Check the horizontal combinations
4   5   6   # --> Check the vertical combinations
7   8   o   # --> Check diagonal combinations

# Play 1
x   2   3
4   5   6
7   8   o

# Play 1
X   2   x
4   5   6
7   8   o

# Play 1
X   o   x
4   5   6
7   8   o

# Play 1
X   o   x
4   5   6
x   8   o

X   o   x
o   5   6
x   8   o

X   o   x
o   x   6
x   8   o

x   o   x
4   5   6
x   8   o


# How to check for a winner:
# --> Check the horizontal combinations
#   for each horizontal row:
#       if the empty char is in there:
#           continue
#       if all chars are the same in row:  --> def check_for_winner(a, b, c) return X or O or None
#           (option 1: mark each x selection with the number 10 and each o selection with 20
#                      add all items in row and if equals 30 then X wins, 60 0 wins, any thing else is not win)
#           (option 2: val = '{pos1 value}', check if pos2 = {val}, check pos3={val})
#           check the char and call them the winner, then break out
# --> Check the horizontal combinations
#       result = check_for_winner(arr[0,0], arr[1,0], arr[2,0]):
#       if result:
#           print(f'Winner is {result}')
#           break
#       check_for_winner(arr[0,1], arr[1,1], arr[2,1])
#       check_for_winner(arr[0,2], arr[1,2], arr[2,2])
#       for v in [0:3]:
#           check_for_winner(arr[0,v], arr[1,v], arr[2,v])
# --> Check the vertical combinations
#       check_for_winner(arr[0,0], arr[0,1], arr[0,2])
#       check_for_winner(arr[1,0], arr[1,1], arr[1,2])
#       check_for_winner(arr[2,0], arr[2,1], arr[2,2])
#       for h in [0:3]:
#           check_for_winner(arr[h,0], arr[h,1], arr[h,2])
# --> If we got this far then its a stalemate
#       print('Stalemate')
#       for x in [0:3]:
#           check_for_winner(arr[0,0], arr[1,0], arr[2,0])
#
# --> Check diagonal combinations
#       check_for_winner(arr[0,0], arr[1,1], arr[2,2])
#       check_for_winner(arr[2,0], arr[1,1], arr[0,2])

# If x played, then put X in the array's position
# Then when you go to print it out, if it is 10 then print X, if Y print 20

```
