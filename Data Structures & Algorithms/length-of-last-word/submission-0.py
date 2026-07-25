class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_clean = s.strip().split( )
        return len(s_clean[-1])