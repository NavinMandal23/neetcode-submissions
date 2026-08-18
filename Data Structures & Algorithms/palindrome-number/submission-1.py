class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tmp = x
        rev = 0
        while tmp > 0:
            rev = (rev * 10) + (tmp % 10)
            tmp = tmp // 10
        return x == rev