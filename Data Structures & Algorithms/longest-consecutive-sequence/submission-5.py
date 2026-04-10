class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        visit = set()

        max_count = 0

        for num in nums:
            if num in visit:
                continue

            count = 1

            while num + count in nums_set:
                visit.add(num + count)
                count += 1

            max_count = max(count, max_count)


        return max_count