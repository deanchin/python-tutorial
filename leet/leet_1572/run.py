def get_diag_sum(arr):
    sum = 0
    y = len(arr)
    for x in range(len(arr)):
        y -= 1
        sum += arr[x][x]
        sum += arr[x][y]
    return sum

# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
mat = [[1,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]]  
mat = [[5]]


result = get_diag_sum(mat)
mat_len = len(mat)
if mat_len % 2 != 0:
    mid = int(mat_len / 2)
    result = result - mat[mid][mid]
print(result)

# print(get_first_diag_sum(mat))
# print(get_second_diag_sum(mat))
# print(get_diag_sum(mat))
    


