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
