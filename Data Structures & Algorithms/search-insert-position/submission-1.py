class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            print(f'L = {L}; R = {R}; mid = {mid}')
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
        # print(f'L = {L}; R = {R}; mid = {mid}')
        if target < nums[mid]:
            return mid 
        else:
            return mid + 1 