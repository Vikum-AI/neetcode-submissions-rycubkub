class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exist = set()

        for num in nums:
            exist.add(num)

        for i in range(0, len(nums)):
            if i not in exist:
                return i

        return len(nums)