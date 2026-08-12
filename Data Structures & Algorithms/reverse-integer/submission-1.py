class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        sign = x // abs(x)    
        tmp = abs(x)
        rev = 0
        while tmp > 0:
            rev = rev * 10 + tmp % 10
            tmp = tmp // 10

        return rev * sign if -2**31 <= rev * sign <= 2**31 else 0