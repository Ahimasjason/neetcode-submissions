class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        rv  = []

        def __recr(open, close, prefix):

            if open > 0 :
                __recr(open -1, close, prefix + "(")
            
            if open < close:
                __recr(open , close -1 , prefix + ")")

            if not close:
                rv.append(prefix)
        __recr(n,n,"")
        return rv