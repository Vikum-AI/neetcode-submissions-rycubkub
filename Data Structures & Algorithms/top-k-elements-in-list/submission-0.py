import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        freq = [-val for val in hash_map.values()]
        heapq.heapify(freq)

        value = None

        for i in range(k):
            value = -heapq.heappop(freq)

        print(value)

        res = []

        for key, val in hash_map.items():
            if val >= value:
                res.append(key)

        return res

        

