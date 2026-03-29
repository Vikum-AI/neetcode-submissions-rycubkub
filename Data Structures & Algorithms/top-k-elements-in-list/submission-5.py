

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        max_heap = [-val for val in hash_map.values()]
        heapq.heapify(max_heap)

        frq = 0

        for i in range(k):
            element = heapq.heappop(max_heap)
            frq = element

        frq = abs(frq)
        res = []

        for key, val in hash_map.items():
            if val >= frq:
                res.append(key)

        return res


        

        
