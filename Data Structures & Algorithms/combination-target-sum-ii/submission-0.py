class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        def __recr(idx , partial, need):
            if need == 0:
                rv.append(partial[:])
                return 
            
            for j in range(idx, len(candidates)):
                if j > idx and candidates[j] == candidates[j -1]:
                    continue 
                if candidates[j] > need:
                    return
                partial.append(candidates[j])
                __recr(j + 1, partial, need - candidates[j])
                partial.pop()



        rv = []
        __recr(0, [], target)
        return rv