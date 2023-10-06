def is_valid_move(board, next_row, next_column):
    if (next_row >= 0 and next_row < len(board)):
        if (next_column >= 0 and next_column < len(board[0])):
            if (board[next_row][next_column] == 0):
                return True 
    return False
