class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 1; R = len(numbers)

        while L < R:
            if numbers[L-1] + numbers[R-1] == target:
                return [L, R]
            elif numbers[L-1] + numbers[R-1] > target:
                R -= 1
            else:
                L += 1
        