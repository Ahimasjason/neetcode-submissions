class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        rv = []
        nums.sort()

        def __recr(idx, partial):
            
            if idx >= len(nums):
                rv.append(partial[:])
                return
            partial.append(nums[idx])
            __recr(idx + 1, partial)
            partial.pop()
            next_idx = idx
            while next_idx + 1 < len(nums) and nums[next_idx] == nums[next_idx + 1]:
                next_idx += 1
            
            
            __recr(next_idx + 1, partial)

        __recr(0, [])
        return rv