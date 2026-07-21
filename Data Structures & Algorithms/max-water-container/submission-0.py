class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i, a in enumerate(heights):
            for j in range(i + 1, len(heights)):
                min_height = min(a, heights[j])
                area = min_height * (j - i)
                if area > maxArea:
                    maxArea = area
        return maxArea