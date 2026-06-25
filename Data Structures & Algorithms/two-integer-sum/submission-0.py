class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution: List[int] = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    if i < j:
                        solution.append(i)
                        solution.append(j)
                    else:
                        solution.append(j)
                        solution.append(i)
                    return solution