class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 1, len(heights) 
        max_water = 0
        while L < R:
            length = R - L
            height = min(heights[L-1],  heights[R-1])
            max_water = max(max_water, length * height)
            if heights[L-1] < heights[R-1]:
                L += 1
            else:
                R -= 1
            print(length, height)
        return max_water