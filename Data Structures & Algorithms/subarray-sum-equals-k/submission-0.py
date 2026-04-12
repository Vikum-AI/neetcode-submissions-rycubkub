class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        res = 0
        total = 0

        for num in nums:
            total += num
            value = total - k
            res += prefix_map[value]

            prefix_map[total] += 1

        return res