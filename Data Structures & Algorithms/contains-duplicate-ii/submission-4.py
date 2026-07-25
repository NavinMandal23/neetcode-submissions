class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        x = len(nums)
        for i, num in enumerate(nums):
            window = nums[i+1: min(i+k+1, x)]
            if num in window:
                return True
        return False
