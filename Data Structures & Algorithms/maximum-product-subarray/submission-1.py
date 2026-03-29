class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minSum, maxSum = 1, 1

        for num in nums:
            tmp = maxSum
            maxSum = max(maxSum * num, minSum * num, num)
            minSum = min(tmp * num, minSum * num, num)
            res = max(res, maxSum)

        return res