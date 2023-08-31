def solution(board):
    template = {str(i): False for i in range(0, 10)}
    squares = [[],[],[],[],[],[],[],[],[]]
    
    # print("Now for rows")
    for i in range(0, 9):
        curr = template.copy()
        if i < 3:
            square_row_offset = 0
        elif i < 6:
            square_row_offset = 3
        else:
            square_row_offset = 6
        
        for j in range(0, 9):
            if board[i][j] == ".":
                continue
            
            if curr[board[i][j]]:
                return False
            curr[board[i][j]] = True
            
            ### setting up square
            if j < 3:
                square_col_offset = 0
            elif j < 6:
                square_col_offset = 1
            else:
                square_col_offset = 2
                
            square_index = square_row_offset + square_col_offset
            squares[square_index].append(board[i][j])
    
    # print("Now for columns")
    for i in range(0, 9):
        curr = template.copy()
        for j in range(0, 9):
            if board[j][i] == ".":
                continue
            if curr[board[j][i]]:
                return False
            curr[board[j][i]] = True
    
    # print("Now for squares")
    for i in range(0, 9):
        curr = template.copy()
        for num in squares[i]:
            if curr[num]:
                return False
            curr[num] = True
    
    return True


if __name__ == "__main__":
    print(solution(
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    ))                                              # true
    
    print(solution(
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    ))                                              # false
