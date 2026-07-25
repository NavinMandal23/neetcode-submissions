class Solution:
    def scoreOfString(self, s: str) -> int:
        ords = []
        for ch in s:
            ords.append(ord(ch))

        score = 0
        for i in range(1, len(ords)):
            score += abs(ords[i] - ords[i-1])
        return score