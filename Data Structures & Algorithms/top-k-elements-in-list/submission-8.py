import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = defaultdict(int)

        for num in nums:
            nums_map[num] += 1

        nums_heap = [-num for num in nums_map.values()]
        heapq.heapify(nums_heap)

        freq = 0

        for i in range(k):
            freq = heapq.heappop(nums_heap)

        freq = abs(freq)
        res = []

        for key, value in nums_map.items():
            if value >= freq:
                res.append(key)

        return res