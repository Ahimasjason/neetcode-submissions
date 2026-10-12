class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        t_counter = Counter(t)
        lp = 0
        wc = Counter()
        min_win = -1,-1
        have_t = 0
        current_min =  len(s) + 1
        for rp in  range(len(s)):
            wc[s[rp]] += 1
            
            if s[rp] in t_counter and wc[s[rp]] == t_counter[s[rp]]:
                have_t += 1
            while have_t == len(t_counter) :
                # shrink

                # ne = (l, r +1)
                if (rp - lp + 1) < current_min:
                    min_win = lp, rp + 1
                    current_min = (rp - lp + 1)


                wc[s[lp]] -= 1
                
                if s[lp] in t_counter and wc[s[lp]]  < t_counter[s[lp]]:
                    have_t -= 1
                lp += 1

        if min_win == (-1,-1):
            return ""
        return s[min_win[0]:min_win[1]]
                    


