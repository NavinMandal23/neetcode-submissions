class Solution:
    def isHappy(self, n: int) -> bool:

        def square_of_digits(num):
            res = 0
            tmp = num
            while tmp > 0:
                res += (tmp % 10) ** 2
                tmp = tmp // 10
            return res

        seen = set()
        x = square_of_digits(n)
        while x != 1: 
            if x in seen:
                return False
            seen.add(x)
            x = square_of_digits(x)
        return True