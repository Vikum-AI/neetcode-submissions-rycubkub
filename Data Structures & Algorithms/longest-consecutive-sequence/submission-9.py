class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hash_set = set(nums)

        for num in nums:
            if num - 1 not in hash_set:
                count = 1
                while num + count in hash_set:
                    count += 1
                
                res = max(res, count)

        return res