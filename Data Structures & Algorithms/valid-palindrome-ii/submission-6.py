class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        L, R = 0, len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return is_palindrome(L+1, R) or is_palindrome(L, R-1)
            L += 1
            R -= 1

        return True
        