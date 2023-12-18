class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            dic_r = {}  
            dic_c = {}  

            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in dic_r:
                        return False
                    dic_r[board[i][j]] = 1

                if board[j][i] != ".":
                    if board[j][i] in dic_c:
                        return False
                    dic_c[board[j][i]] = 1

        for k in range(3):
            for l in range(3):
                dic_g = {}  
                for i in range(3 * k, 3 * k + 3):
                    for j in range(3 * l, 3 * l + 3):
                        if board[i][j] != ".":
                            if board[i][j] in dic_g:
                                return False
                            dic_g[board[i][j]] = 1

        return True
# https://leetcode.com/problems/valid-sudoku/submissions/1107178621/