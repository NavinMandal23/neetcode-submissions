class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        heapq.heapify(heap)
        
        for pi in points:
            xi, yi = pi[0], pi[1]
            dist = -1 * ((xi ** 2) + (yi ** 2)) # ** 0.5 not needed as sqrt is monotonically increasing anyway

            heapq.heappush(heap, (dist, pi))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [p for d, p in heap]
        