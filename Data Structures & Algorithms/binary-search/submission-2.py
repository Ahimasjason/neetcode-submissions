class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        lo, hi = 0, len(nums) -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            n = nums[mid]
            if  n == target:
                return mid

            if n > target:
                hi = mid -1
            else:
                lo = mid + 1
        return -1