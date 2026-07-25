class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mco, cco = 0, 0
        for num in nums:
            if num == 1:
                cco += 1
            else:
                mco = max(mco, cco)
                cco = 0 
        return max(mco, cco)