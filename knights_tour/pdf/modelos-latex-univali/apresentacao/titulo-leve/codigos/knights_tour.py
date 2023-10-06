def knights_tour(board_size, initial_row, initial_column):
    board = []
    initialize_board(board, board_size)
    board[initial_row][initial_column] = 0
    
    if (solve_knights_tour(board, initial_row, initial_column, 1)):
        print_board(board)
        return True 
    
    print("No solution found")
    return False
