class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            if j >= len(nums):
                break

            while j < len(nums) and j != k:
                if nums[j] + nums[k] == -nums[i]:
                    this_lst = [nums[i], nums[j], nums[k]]
                    if this_lst not in answer:
                        answer.append(this_lst)
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    j += 1
        return answer