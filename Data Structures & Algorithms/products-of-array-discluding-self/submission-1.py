class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix_arr = []
        suffix_arr = []
        for i in range(len(nums)):
            product = 1
            j = 0
            while j < i:
                product *= nums[j]
                j += 1
            prefix_arr.append(product)
        
        for i in range(len(nums)):
            product = 1
            j = i + 1
            while j < len(nums):
                product *= nums[j]
                j += 1
            suffix_arr.append(product)

        for i in range(len(nums)):
            output.append(prefix_arr[i] * suffix_arr[i])
        return output

