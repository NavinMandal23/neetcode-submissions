class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        window = set()
        n = len(nums)
        for R in range(n):
            if R - L > k: # check window size is bigger
                window.remove(nums[L]) 
                L += 1
            if nums[R] in window: # check duplicates in valid window
                return True
            window.add(nums[R])
        return False