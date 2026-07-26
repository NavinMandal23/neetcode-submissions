class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_mj = nums[0]
        cnt = 0

        for num in nums:
            if cnt == 0:
                curr_mj = num
            
            cnt += (1 if num == curr_mj else -1)
        
        return curr_mj