def initialize_board(board, board_size):
    for row in range(board_size):
        a = []
        for column in range(board_size):
            a.append(0)
        board.append(a)
