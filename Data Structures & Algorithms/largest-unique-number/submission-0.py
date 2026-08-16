class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        res = -float('inf')
        for k, v in c.items():
            if v == 1:
                res = max(res, k)
        return -1 if res == -float('inf') else res