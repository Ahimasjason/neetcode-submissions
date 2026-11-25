class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        seen = set()

        def dfs(r, c, offset):
            if offset == len(word):return True
            if (r, c) in seen:return False
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[offset]:
                return False 
            seen.add((r,c))
            found = (
                dfs(r , c + 1, offset + 1) or
                dfs(r, c -1 , offset + 1) or
                dfs(r + 1, c, offset + 1) or 
                dfs(r - 1, c, offset + 1)
            )

            seen.remove((r,c))
            return found

                        

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r,c, 0):return True

        return False