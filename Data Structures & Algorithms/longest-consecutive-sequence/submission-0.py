class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                this_length = 1
                start = num
                while start + 1 in nums_set:
                    this_length += 1
                    start += 1
                if this_length > length:
                    length = this_length
        return length
