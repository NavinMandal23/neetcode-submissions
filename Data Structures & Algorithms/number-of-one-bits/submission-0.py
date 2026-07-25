class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = n
        bits = 0
        while temp > 0: 
            if temp % 2 == 1:
                bits += 1 
            temp = temp >> 1 # 32 bits so max 32 O(1) right shifts
        return bits