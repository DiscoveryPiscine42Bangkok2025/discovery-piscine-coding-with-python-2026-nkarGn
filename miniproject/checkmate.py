def checkmate(board):
    

    row = 0
    column = 0
    for i in board:
        if i != '\n':
            column += 1
        else:
            break
    row = len(board.splitlines())
    board_no_newline = board.replace('\n', '')
    new_board = []
    print(f"columns: {column} , rows: {row}")

    if row != column:
        print("Error: the board is not square")
        return
    if board.count('K') != 1:
        print("Error: there must be exactly one King on the board")
        return
    for i in range(row):
        new_board.append([])
        for j in range(column):
            new_board[i].append(board_no_newline[i * column + j])
    rook_positions = (0, 0)
    queen_positions = (0, 0)
    pawn_positions = (0, 0)
    king_positions = (0, 0)
    for i in range(row):
        for j in range(column):
            if new_board[i][j] == 'R':
                rook_positions = (i, j)
                new_board = rook_rewrite(new_board, rook_positions[0] , rook_positions[1])
            if new_board[i][j] == 'Q':
                queen_positions = (i, j)
                new_board = queen_rewrite(new_board, queen_positions[0] , queen_positions[1])
            if new_board[i][j] == 'P':
                pawn_positions = (i, j)
                new_board = pawn_rewrite(new_board, pawn_positions[0] , pawn_positions[1])
            if new_board[i][j] == 'K':
                king_positions = (i, j)
                


    
    print("Rook positions:", rook_positions)
    print("New board after rook rewrite:")
    for row in new_board:
        print(row)

    if check_king(new_board):
        print("Success")
    else:  
        print("Fail")

    



def rook_rewrite(new_board, rook_r, rook_c): 
    board_rows = len(new_board)     
    board_cols = len(new_board[0])   

    for i in range(board_rows): 
        for j in range(board_cols):
            if i == rook_r or j == rook_c: 
                if not (i == rook_r and j == rook_c): 
                    new_board[i][j] = 'X'
                    print(f"Rook can attack position: ({i}, {j})")
    return new_board


def queen_rewrite(new_board, queen_r, queen_c): 
    board_rows = len(new_board)     
    board_cols = len(new_board[0])   

    for i in range(board_rows): 
        for j in range(board_cols):
            if i == queen_r or j == queen_c or abs(queen_r - i) == abs(queen_c - j): 
                if not (i == queen_r and j == queen_c): 
                    new_board[i][j] = 'X' 
                    print(f"Queen can attack position: ({i}, {j})")
    return new_board

def pawn_rewrite(new_board, pawn_r, pawn_c): 
    board_rows = len(new_board)     
    board_cols = len(new_board[0])   

    attack_positions = [(pawn_r - 1, pawn_c - 1), (pawn_r - 1, pawn_c + 1)] 

    for pos in attack_positions:
        r, c = pos
        if 0 <= r < board_rows and 0 <= c < board_cols:
            new_board[r][c] = 'X' 
            print(f"Pawn can attack position: ({r}, {c})")
    return new_board

def bishop_rewrite(new_board, bishop_r, bishop_c): 
    board_rows = len(new_board)     
    board_cols = len(new_board[0])   

    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] 

    for direction in directions:
        dr, dc = direction
        r, c = bishop_r + dr, bishop_c + dc
        while 0 <= r < board_rows and 0 <= c < board_cols:
            new_board[r][c] = 'X' 
            print(f"Bishop can attack position: ({r}, {c})")
            r += dr
            c += dc
    return new_board  

def check_king(new_board):
    for i in new_board:
        for j in i:
            if j == 'K':
                return False
    return True
   
    


    
