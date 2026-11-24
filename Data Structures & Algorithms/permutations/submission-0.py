class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def __recr(idx):
            if idx == len(nums) -1:
                rv.append(nums[:])
                return

            
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i] , nums[idx]
                __recr(idx + 1)
                nums[idx], nums[i] = nums[i] , nums[idx]

        rv = []
        __recr(0)
        return rv