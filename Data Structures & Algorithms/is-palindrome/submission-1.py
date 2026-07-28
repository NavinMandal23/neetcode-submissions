class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_str = ''
        for char in s.lower():
            if char.isalnum():
                normalized_str += char
        return normalized_str == normalized_str[::-1]