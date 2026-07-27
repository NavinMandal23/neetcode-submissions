class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lc = 0
        numset = set(nums)
        lcs = 0
        ccs = 0
        for n in numset:
            ccs = 1
            x = n
            while x-1 in numset:
                ccs += 1
                x = x-1
            lcs = max(lcs, ccs)
        return max(lcs, ccs)