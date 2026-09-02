class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        for i in strs :

            sorti = "".join(sorted(i))
            
            d[sorti].append(i)

        return list(d.values())
