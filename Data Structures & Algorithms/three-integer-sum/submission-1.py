class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zero_count = 0
        for i in nums:
            if i == 0:
                zero_count += 1

        num_set = set(nums)
        answers = []
        answer_sets = []

        if zero_count >= 3:
            answers.append([0,0,0])

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    two_sum = nums[i] + nums[j]
                    if -two_sum != nums[i] and -two_sum != nums[j] and -two_sum in num_set:
                        if set([nums[i], nums[j], -two_sum]) in answer_sets:
                            continue
                        answers.append([nums[i], nums[j], -two_sum])
                        answer_sets.append(set([nums[i], nums[j], -two_sum]))
        return answers