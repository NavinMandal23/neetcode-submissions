class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x = len(nums)
        nums.sort() 
        res = []

        for i in range(0, x-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                L = i+1
                R = x-1
                while L < R:
                    if nums[L] + nums[R] + nums[i] == 0:
                        res.append([nums[i], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L+1] and nums[R] == nums[R-1]:
                            L += 1
                            R -= 1
                        L+=1
                        R-=1
                        continue
                        
                    elif nums[L] + nums[R] + nums[i] > 0:
                        R -= 1
                    else:
                        L += 1
        return res