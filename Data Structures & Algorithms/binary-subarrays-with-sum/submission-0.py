class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        res = 0
        curSum = 0

        for num in nums:
            curSum += num
            res += prefix_map[curSum - goal]
            prefix_map[curSum] += 1

        return res
