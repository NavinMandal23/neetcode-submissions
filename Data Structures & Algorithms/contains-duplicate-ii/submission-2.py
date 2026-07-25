class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        x = len(nums)
        for i in range(x):
            for j in range(i+1, x):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        return False