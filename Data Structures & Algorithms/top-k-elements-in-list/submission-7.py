

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        max_heap = [-val for val in counts.values()]
        heapq.heapify(max_heap)

        freq = 1

        for i in range(k):
            freq = heapq.heappop(max_heap)

        res = []
        freq = abs(freq)

        for key, val in counts.items():
            if val >= freq:
                res.append(key)

        return res
        
