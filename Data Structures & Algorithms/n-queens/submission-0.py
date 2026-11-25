class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        def is_valid(row, col, board):
            #  check for all the above row on the same col
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            
            #  left diagonal check
            r,c = row -1, col -1

            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r-=1
                c-=1

            r,c = row -1, col +1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False

                r = r - 1
                c = c + 1


            return True

        tmp = [['.' for _ in range(n)] for _ in range(n)]
        
        def dfs(row):
            if row == n:
                t = []
                for r in range(n):
                    t.append("".join(tmp[r]))
                rv.append(t)
                return


            for c in range(n):
                if is_valid(row, c, tmp):
                    tmp[row][c] = "Q"
                    dfs(row + 1)
                    tmp[row][c] = "."
                    
        rv = []
        dfs(0)
        return rv

