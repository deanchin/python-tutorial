
def minTimeToVisitAllPoints(points):

    moves = []
    for point in points:
        # print(f'Processing point {point}')
        if not moves:
            moves.append(point)
            continue

        curr_pos = moves[len(moves) - 1]

        while curr_pos != point:
            curr_x = curr_pos[0]
            curr_y = curr_pos[1]

            # Get next x
            if curr_x < point[0]:
                next_x = curr_x + 1
            elif curr_x > point[0]:
                next_x = curr_x - 1
            else:
                next_x = curr_x

            # Get next y
            if curr_y < point[1]:
                next_y = curr_y + 1
            elif curr_y > point[1]:
                next_y = curr_y - 1
            else:
                next_y = curr_y

            moves.append([next_x, next_y])
            curr_pos = [next_x, next_y]

    return moves


print(
    minTimeToVisitAllPoints(
        [[1, 1], [3, 4], [-1, 0]]
    )
)