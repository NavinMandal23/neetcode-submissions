class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        c1 = Counter(s1)
        L, R = 0, len(s1)

        while R <= len(s2):
            # print(s1, s2[L:R])
            c2 = Counter(s2[L:R])
            if c1 == c2:
                return True
            L += 1
            R += 1
        return False
