class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        x = len(nums)
        k = k % x
        reverse(0, x - 1)
        reverse(0, k - 1)
        reverse(k, x - 1)