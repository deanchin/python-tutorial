import numpy as np

TABLE = np.zeros((6, 7), dtype=int)
win1rule = np.array([1,1,1,1])
win2rule = np.array([2,2,2,2])

# arr = [0,0,1,1,1,1,2,2,1,1,0]
arr = [0,0,1,1,1,1,2,2,1,1,0]
sub_arrays = [arr[i:i+4] for i in range(len(arr)-3)] 

for sub in sub_arrays:
    print(sub)

player1wins = any([np.array_equal(win1rule, sub) for sub in sub_arrays])
player2wins = any([np.array_equal(win2rule, sub) for sub in sub_arrays])

TABLE[2,1] = 1
TABLE[3,2] = 1
TABLE[4,3] = 1
TABLE[5,4] = 1

diags = []
i = 7
j = 6
diags.append(np.diagonal(TABLE, offset=(j - i)))
diags.append(np.diagonal(np.rot90(TABLE), offset=-TABLE.shape[1] + (j + i) + 1))
print("---------------")
print("rotrot")
print(np.rot90(TABLE))
print(TABLE)
print("*********************")
for i in diags:
    print(list(i))
print("---------------")

if player1wins:
    print('Player 1 wins')
elif player2wins:
    print('Player 2 wins')
else:
    print('Tie')

win_length = 4
r = 8
c = 10
a = np.arange(r * c).reshape(r,c)
print(a)
# print(a.diagonal(c - win_length))
for i in range(0,c - win_length + 1):
    print(a.diagonal(i))
    print(a.diagonal(-i))
print("==============================")
for i in range(0,r - win_length + 1):
    print(np.diagonal(np.rot90(a), i))
# print(np.diagonal(np.rot90(a)))