class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0:1}
        res = 0
        curr_psum = 0
        for num in nums:
            curr_psum += num
            if curr_psum - k in prefix_sums:
                res += prefix_sums[curr_psum - k]
            prefix_sums[curr_psum] = prefix_sums.get(curr_psum, 0) + 1
        return res