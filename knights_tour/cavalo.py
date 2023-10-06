import sys

def initialize_board(board, board_size):
    for row in range(board_size):
        a = []
        for column in range(board_size):
            a.append(0)
        board.append(a)

def print_board(board):
    for row in board:
        print(row)
    print()

def is_valid_move(board, next_row, next_column):
    if (next_row >= 0 and next_row < len(board)):
        if (next_column >= 0 and next_column < len(board[0])):
            if (board[next_row][next_column] == 0):
                return True 
    return False
       
def solve_knights_tour(board, initial_row, initial_column, move_count):
    if (move_count == (len(board) * len(board[0]))):
        return True
    
    for i in range(8): # number of possible movements in L
        next_row = initial_row + x_moves[i]
        next_column = initial_column + y_moves[i]

        if (is_valid_move(board, next_row, next_column)):
            board[next_row][next_column] = move_count
            if (solve_knights_tour(board, next_row, next_column, move_count + 1)):
                return True
            board[next_row][next_column] = 0
    
    return False

def knights_tour(board_size, initial_row, initial_column):
    board = []
    initialize_board(board, board_size)
    board[initial_row][initial_column] = 0
    
    if (solve_knights_tour(board, initial_row, initial_column, 1)):
        print_board(board)
        return True 
    
    print("No solution found")
    return False
    
x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

print("### Knight's tour ###")

size = int(input("\n Choose board size (NxN)\n"))

if (size <= 3):
    print("Size must be greater than 3")
    sys.exit()


x = int(input("\n Choose initial X position\n"))
y = int(input("\n Choose initial y position\n"))

if not ((x >= 0 and x < size) and (y >= 0 and y < size)):
    print("Inititial position must be within board limits") 
    sys.exit() 


knights_tour(size, x, y)
