class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def directed_permutation(idx, partial):
            if idx == len(s):
                rv.append(partial[:])
                return


            
            for i in range(idx + 1, len(s) + 1):
                word = s[idx : i]
                if word[::-1] == word:
                    directed_permutation(i,  partial + [word])

        rv = []
        directed_permutation(0,[])
        return rv
        