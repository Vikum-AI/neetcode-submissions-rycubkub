

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        max_heap = [-val for val in hash_map.values()]
        heapq.heapify(max_heap)

        freq = 1

        for i in range(k):
            freq = heapq.heappop(max_heap)

        freq = abs(freq)

        res = []

        for key, val in hash_map.items():
            if val >= freq:
                res.append(key)

        return res

        
