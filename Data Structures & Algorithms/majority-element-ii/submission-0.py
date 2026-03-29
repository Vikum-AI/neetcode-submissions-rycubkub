class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        n = len(nums) 
        freq = n // 3
        res = []

        for key, val in hash_map.items():
            if val > freq:
                res.append(key)

        return res