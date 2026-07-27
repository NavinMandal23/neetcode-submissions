class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lc = 0
        numset = set(nums)
        lcs = 0
        ccs = 0
        for n in numset:
            if n - 1 not in numset: # this could be a starting point for the sequence
                ccs = 1
                while n + ccs in numset:
                    ccs += 1
            lcs = max(lcs, ccs)
        return lcs