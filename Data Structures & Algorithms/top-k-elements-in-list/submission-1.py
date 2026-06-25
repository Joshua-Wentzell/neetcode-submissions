class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for i in range(k,0,-1):
            sorted_lst = sorted(counts.items(), key=lambda item: item[1])
            results.append(sorted_lst[-i][0])
            del sorted_lst[-i]

        return results