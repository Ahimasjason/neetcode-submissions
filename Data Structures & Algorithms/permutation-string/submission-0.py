class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        from collections import Counter

        if len(s1) > len(s2):return False

        r = len(s1)
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])
        if s1_counter == s2_counter: return True
        l = 0
        while r < len(s2):
            s2_counter[s2[r]] += 1
            s2_counter[s2[l]] -= 1
            if s1_counter == s2_counter: return True
            l += 1
            r += 1
        return False





        
        # if len(s1) > len(s2):return False

        # r = 0
        # l = len(s1) -1

        # while r < len(s2):
        #     print(s1[l] , s2[r])
        #     while l > 0 and s1[l] == s2[r]:
        #         r += 1
        #         l -= 1
        #     print(l, r)
        #     if l < 0:return True
        #     l = len(s1) -1
        #     r += 1

        # return False
        