
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        p1 = 0

        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums) - 1

            while l < r:
                diff = a + nums[l] + nums[r]

                if diff > 0:
                    r -= 1
                elif diff < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < len(nums) and nums[l-1] == nums[l]:
                        l += 1
                
        return res
                
