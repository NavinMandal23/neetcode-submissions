class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = len(nums)
        return sorted(nums)[x//2]