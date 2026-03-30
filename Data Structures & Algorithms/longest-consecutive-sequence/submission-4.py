class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 1 if len(nums) > 1 else 0

        for num in nums:
            count = 1
            value = num
            while num + count in nums_set:
                count += 1

            max_count = max(max_count, count)

        return max_count
