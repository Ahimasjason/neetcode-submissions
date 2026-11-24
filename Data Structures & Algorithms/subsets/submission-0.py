class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rv = []
        def __recr(idx, partial):
            if idx == len(nums):
                rv.append([i for i in partial])
                return
            
            # run without the 
            __recr(idx + 1, partial)
            partial.append(nums[idx]);
            __recr(idx + 1, partial)
            partial.pop()
            return

        __recr(0, [])
        return rv

        