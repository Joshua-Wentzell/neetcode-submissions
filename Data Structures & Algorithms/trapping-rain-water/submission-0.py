class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0
        height_length = len(height)
        for i, a in enumerate(height):
            max_left, max_right = a, a
            max_left_ind, max_right_ind = i, i
            l = i - 1
            r = i + 1
            while l >= 0:
                if height[l] > max_left:
                    max_left = height[l]
                    max_left_ind = l
                l -= 1

            while r < height_length:
                if height[r] > max_right:
                    max_right = height[r]
                    max_right_ind = r
                r += 1

            if max_left > a and max_right > a:
                max_area += min(max_left, max_right) - a
        return max_area
