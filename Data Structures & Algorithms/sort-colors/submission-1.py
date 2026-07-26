class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L, R = 0, len(nums) - 1
        i = 0
        
        while i <= R:
            # print(L, R, i)
            if nums[i] == 0:
                nums[i], nums[L] = nums[L], nums[i]
                L += 1
            elif nums[i] == 2:
                # we are swapping in an unseen value from the right,
                # so we can't increment i until we see/process it
                nums[i], nums[R] = nums[R], nums[i] 
                R -= 1
                i -= 1
            i += 1
            
        