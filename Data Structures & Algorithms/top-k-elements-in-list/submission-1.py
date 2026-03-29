import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        freq_heap = [-val for val in hash_map.values()]
        heapq.heapify(freq_heap)

        print(freq_heap)

        freq = 0

        for i in range(k):
            freq = heapq.heappop(freq_heap)

        res = []
        freq = abs(freq)

        print(hash_map)

        for key, val in hash_map.items():
            if val >= freq:
                res.append(key)

        return res

