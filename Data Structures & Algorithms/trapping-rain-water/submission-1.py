class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0
        height_length = len(height)
        leftMax = []
        rightMax = []
        maxSoFar = height[0]
        for i, a in enumerate(height):
            if a >= maxSoFar:
                maxSoFar = a
            leftMax.append(maxSoFar)

        maxSoFar = height[height_length - 1]
        for i in range(height_length - 1, -1, -1):
            if height[i] >= maxSoFar:
                maxSoFar = height[i]
            rightMax.append(maxSoFar)

        rightMax.reverse()
        for i, a in enumerate(height):
            max_area += min(leftMax[i], rightMax[i]) - a
        return max_area