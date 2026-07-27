class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # numbers should be within 1 to arr length, not out of range / too small or large
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]: 
                xi = nums[i] - 1 # expected index
                nums[i], nums[xi] = nums[xi], nums[i] # swap current element with its expected index

        for i, num in enumerate(nums, 1):
            if i != num:
                return i
        return n+1