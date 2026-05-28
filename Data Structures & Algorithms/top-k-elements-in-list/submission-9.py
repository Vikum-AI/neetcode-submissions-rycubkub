class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1
        
        max_heap = [-value for value in hash_map.values()]
        heapq.heapify(max_heap)

        freq = None

        for i in range(k):
            freq = heapq.heappop(max_heap)

        res = []
        freq = abs(freq)

        for key, value in hash_map.items():
            if value >= freq:
                res.append(key)

        return res