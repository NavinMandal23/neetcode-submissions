class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        counter = Counter(nums)
        arr = []
        for key, count in counter.items():
            arr.append((-count, key))
        heapq.heapify(arr)

        res = []
        for i in range(k):
            x = heapq.heappop(arr)
            res.append(x[1])
        return res