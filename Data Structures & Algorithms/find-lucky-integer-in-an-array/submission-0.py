class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        res = -1
        c = Counter(arr)
        for k,v in c.items():
            if k == v:
                res = max(res, k)
        return res