class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        ctr = Counter(nums)
        for k,v in ctr.items():
            if v > 1:
                return True
        return False