class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0, 20:0}
        
        for b in bills:
            change[b] += 1
            remainder = b - 5
            if remainder == 15:
                if change.get(10) >= 1 and change.get(5) >= 1:
                    change[10] -= 1
                    change[5] -= 1
                elif change.get(5) >= 3:
                    change[5] -= 3
                else:
                    return False
            elif remainder == 10:
                if change.get(10) >= 1:
                    change[10] -= 1
                elif change.get(5) >= 2:
                    change[5] -= 2
                else:
                    return False
            elif remainder == 5:
                if change.get(5) >= 1:
                    change[5] -= 1
                else:
                    return False
            else:
                continue
        return True
