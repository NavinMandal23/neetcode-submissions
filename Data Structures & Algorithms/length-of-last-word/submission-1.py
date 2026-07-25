class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_clean = s.strip()
        res = 0
        print(s_clean[::-1])
        for ch in s_clean[::-1]:
            if ch.isalpha():
                res += 1
            else:
                return res
        return res