class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp, rp = [1], []
        x = len(nums)

        leftprod = 1
        for i in range(0, x - 1):
            lp.append(nums[i] * leftprod)
            leftprod *= nums[i]

        rightprod = 1
        for j in range(x - 1, 0, -1):
            rp.append(nums[j] * rightprod)
            rightprod *= nums[j]
        rp.reverse()
        rp.append(1)
        
        res = []
        for k in range(x):
            res.append(lp[k] * rp[k])
        return res
