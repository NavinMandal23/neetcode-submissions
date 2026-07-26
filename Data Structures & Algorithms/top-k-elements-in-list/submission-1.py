class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums)

        result = []
        for key,value in sorted(counter.items(), key=lambda x: -x[1]):
            result.append(key)
        return result[:k]