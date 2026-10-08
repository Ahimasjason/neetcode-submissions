class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        d = defaultdict(int)

        l = 0

        max_val = 0
        for r in range(0, len(s)):

            #  add the current r to the dict
            d[s[r]] += 1
            


            while (r - l + 1) - max(d.values()) > k :
                d[s[l]] -= 1
                l += 1
                

            max_val = max(max_val, r - l + 1)

        return max_val