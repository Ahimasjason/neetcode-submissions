class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        max_val  = max(piles)
        mim_val = max_val

        l, r = 1, max_val
        while l <= r:
            mid = l + (r - l ) // 2

            time = 0
            # try to eat banana at this rate
            for i in piles:
                time += math.ceil(i/mid)

            if time <= h:
                # successfully eaten within the time
                r  = mid - 1
                mim_val = mid
            else:
                l = mid + 1

            
            # now decide which way to go 

        return int(mim_val)