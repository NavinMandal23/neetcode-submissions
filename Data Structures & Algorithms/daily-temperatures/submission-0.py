class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        i = 0
        while i < n:
            if len(stack) == 0:
                stack.append((temperatures[i], i))
            elif temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
            else: # warmer day observed
                while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                    prev_day = stack.pop()
                    res[prev_day[1]] = i - prev_day[1]
                continue
            i+=1
        return res