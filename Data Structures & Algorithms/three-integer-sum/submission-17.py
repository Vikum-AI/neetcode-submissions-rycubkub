class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #    [-1,0,1,2,-1,-4]
        #    [-4, -1, -1, 0, 1, 2]
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]

                if three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return res