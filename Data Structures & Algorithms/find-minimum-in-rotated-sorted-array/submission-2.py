class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        p1 = 0
        p2 = len(nums) - 1

        min_val = float('inf')

        while p2 > p1:
            mid = (p1 + p2) // 2
            min_val = min(min_val, nums[p1], nums[p2], nums[mid])

            if nums[p1] < nums[mid]:
                p1 = mid + 1
            else:
                p2 = mid - 1


        return min_val
            

            


