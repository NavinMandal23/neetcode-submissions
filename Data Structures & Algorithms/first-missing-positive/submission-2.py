class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            current_num = nums[i]
            # Is current_num is within the range and in the expected index?
            while 1 <= current_num <= n and nums[current_num - 1] != current_num: 
                expected_idx = current_num - 1 
                nums[i], nums[expected_idx] = nums[expected_idx], nums[i] 
                current_num = nums[i]

        for i, num in enumerate(nums, 1):
            if i != num:
                return i
                
        return n + 1