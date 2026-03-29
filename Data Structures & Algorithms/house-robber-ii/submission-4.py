class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0
        for num in nums[1:]:
            tmp = max(num+rob1, rob2)
            rob1 = rob2
            rob2 = tmp

        rob3, rob4 = 0, 0
        for num in nums[:len(nums)-1]:
            tmp = max(num+rob3, rob4)
            rob3 = rob4
            rob4 = tmp

        return max(rob2, rob4)