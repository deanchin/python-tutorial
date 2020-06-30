''' Tic Tac Toe '''


class TicTacToe():
    ''' Tic Tac Toe class '''

    def __init__(self):
        self.current_player = 'X'
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    def show_board(self):
        ''' show board '''
        for row in self.board:
            print(row)
        print()

    def change_player(self):
        ''' change to the next player '''
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def get_player(self):
        ''' return current player '''
        return self.current_player

    def submit_move(self, pos):
        ''' submit move '''
        found = False
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == pos:
                    self.board[row][column] = self.current_player
                    found = True
                    break
            if found:
                break
        if not found:
            print(f'Position {pos} is an invalid move\n')
            return
        self.change_player()


GAME = TicTacToe()

while True:
    GAME.show_board()
    next_move = input(
        f'Player {GAME.get_player()}, Enter your move (1-9 or exit): ')
    if next_move.lower() == 'exit':
        break
    GAME.submit_move(next_move)


# board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
# for row in range(3):
#     for col in range(3):
#         if board[row][col] == '3':
#             print(f'location is [{row}][{col}]')

# List Comprehension Examples
# items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_items = [x if x % 2 else None for x in items]

# new_items = []
# for i in items:
#     if i % 2:
#         new_items.append(i)
#     else:
#         new_items.append(None)


# How would you 