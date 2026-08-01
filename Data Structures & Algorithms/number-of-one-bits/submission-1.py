class Solution:
    def hammingWeight(self, n: int) -> int:
        tmp = n
        count = 0
        while tmp > 0:
            count += (tmp % 2)
            tmp = tmp // 2
        return count