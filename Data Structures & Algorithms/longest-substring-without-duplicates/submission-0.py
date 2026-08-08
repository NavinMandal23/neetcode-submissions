class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        n = len(s)
        max_len = 0
        R = 0
        while R < n:
            if s[R] not in window:
                window.add(s[R])
                max_len = max(max_len, len(window))
            else:
                while s[R] in window:
                    window.remove(s[L])
                    L += 1
                window.add(s[R])
            R += 1
        return max(max_len, len(window))