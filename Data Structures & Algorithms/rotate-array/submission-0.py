class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = len(nums)
        k = k % x

        for i in range(k):
            # rotate right by 1 pos
            nums.insert(0, nums.pop())
        