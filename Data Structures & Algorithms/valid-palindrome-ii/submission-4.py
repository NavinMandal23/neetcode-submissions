class Solution:
    def validPalindrome(self, s: str) -> bool:
        deleted = None
        L, R = 0, len(s) - 1
        while L <= R:
            if s[L] != s[R]:
                deleted = True
                break
            L += 1
            R -= 1

        if deleted == True:
            ldp = s[:L] + s[L+1:]
            rdp = s[:R] + s[R+1:]
            return ldp == ldp[::-1] or rdp == rdp[::-1]
        else:
            return s == s[::-1]
        