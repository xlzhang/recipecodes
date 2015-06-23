class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        row = [[0]*9 for i in range(10)]
        col = [[0]*9 for i in range(10)]
        box = [[0]*9 for i in range(10)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    rc_index = int(board[i][j]) - 1
                    box_index = (i/3)*3 + j/3
                    if row[i][rc_index] or col[j][rc_index] or box[box_index][rc_index]:
                        return False
                    
                    row[i][rc_index] = 1
                    col[j][rc_index] = 1
                    box[box_index][rc_index] = 1
        return True
