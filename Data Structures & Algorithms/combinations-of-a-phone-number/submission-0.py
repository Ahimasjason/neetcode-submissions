class Solution:
    COMB = ["", "abc" ,"def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    def letterCombinations(self, digits: str) -> List[str]:
        if  not digits : return []
        def dfs(idx, partial):
            if idx == len(digits):
                rv.append(partial)
                return

            
            
            for c in self.COMB[int(digits[idx]) -1]:
                dfs( idx + 1, partial + c)


        rv = []
        dfs(0,"")
        return rv

        

        