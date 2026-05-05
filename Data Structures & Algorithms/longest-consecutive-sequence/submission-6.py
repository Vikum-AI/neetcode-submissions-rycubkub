class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)

        for i, num in enumerate(nums):
            if (num - 1) in nums_set:
                continue

            seq_len = 1

            while (num + seq_len) in nums_set:
                seq_len += 1

            max_len = max(max_len, seq_len)

        return max_len

            