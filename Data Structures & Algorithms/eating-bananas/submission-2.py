class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, up = 1, max(piles)

        while lo <= up:
            rate = lo + (up - lo) // 2
            hrs = 0
            for p in piles:
                hrs += (p + rate - 1) // rate
            
            if hrs <= h:
                up =rate -1
            else:
                lo = rate + 1

        return lo
      