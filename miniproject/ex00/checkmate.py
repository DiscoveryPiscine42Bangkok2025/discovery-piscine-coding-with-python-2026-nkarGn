def checkmate(board):

    row = len(board.splitlines()) 
    column = 0
   

    lines = board.splitlines()
    
    if not lines:
        print("Error: empty board")
        return
    
    row = len(lines)
    
    lengths = []
    for line in lines:
        lengths.append(len(line))
    
    if len(set(lengths)) != 1:
        print("Error: the board is not square (rows have different number of pieces/columns)")
        return
    
    column = lengths[0]  
    
    if row != column:
        print(f"Error: not a square board ({row} rows, {column} columns)")
        return


    print(lines)
        

    
    board_no_newline = board.replace('\n', '') 
    new_board = [] 

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
    bishop_positions = (0, 0)
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
            if new_board[i][j] == 'B':
                bishop_positions = (i, j)
                new_board = bishop_rewrite(new_board, bishop_positions[0] , bishop_positions[1])
                


    

    #for row in new_board:
    #   print(row)

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
                    new_board[i][j] = 'X' if new_board[i][j] not in ['R', 'Q', 'P', 'B'] else new_board[i][j]
    return new_board 



def pawn_rewrite(new_board, pawn_r, pawn_c): 
    board_rows = len(new_board)     
    board_cols = len(new_board[0])   

    attack_positions = [(pawn_r - 1, pawn_c - 1), (pawn_r - 1, pawn_c + 1)] 

    for pos in attack_positions: 
        r, c = pos 
        if 0 <= r < board_rows and 0 <= c < board_cols: 
            new_board[r][c] = 'X' if new_board[r][c] not in ['R', 'Q', 'P', 'B'] else new_board[r][c]
    return new_board

def bishop_rewrite(new_board, bishop_r, bishop_c): 
    board_rows = len(new_board)     
    board_cols = len(new_board[0])   

    for i in range(board_rows): 
        for j in range(board_cols):
            if abs(bishop_r - i) == abs(bishop_c - j): 
                if not (i == bishop_r and j == bishop_c): 
                    new_board[i][j] = 'X' if new_board[i][j] not in ['R', 'Q', 'P', 'B'] else new_board[i][j]
    return new_board

def queen_rewrite(new_board, queen_r, queen_c): 
    board_rows = len(new_board)     
    board_cols = len(new_board[0])   

    for i in range(board_rows): 
        for j in range(board_cols):
            if i == queen_r or j == queen_c or abs(queen_r - i) == abs(queen_c - j): 
                if not (i == queen_r and j == queen_c): 
                    new_board[i][j] = 'X' if new_board[i][j] not in ['R', 'Q', 'P', 'B'] else new_board[i][j]
    return new_board

def check_king(new_board):
    for i in new_board: 
        for j in i:
            if j == 'K':
                return False
    return True
   
    


    
