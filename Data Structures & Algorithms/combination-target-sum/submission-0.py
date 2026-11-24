class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        rv = []

        nums.sort()
        def __recr(idx , partial, need):
            if need == 0:
                rv.append(partial[:])

            
            for i in range(idx, len(nums)):
                if nums[i] > need:
                    # nums sorted so no need to go 
                    return
                partial.append(nums[i])
                __recr(i, partial, need - nums[i])
                partial.pop()
        __recr(0, [],target)
        return rv

        