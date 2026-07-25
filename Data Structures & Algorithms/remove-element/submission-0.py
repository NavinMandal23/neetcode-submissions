class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        swappable = len(nums) - 1

        while curr <= swappable:
            if nums[swappable] == val:
                swappable -= 1
                continue
            if nums[curr] == val:
                nums[curr], nums[swappable] = nums[swappable], nums[curr]
                swappable -= 1
            curr += 1
        return swappable + 1
        