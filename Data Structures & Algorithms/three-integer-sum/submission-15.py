class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        # [-4, -1, -1, 0, 1, 2]

        nums.sort()
        res = []

        for p1 in range(len(nums) - 2):
            target = -nums[p1]
            p2, p3 = p1 + 1, len(nums) - 1

            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue


            while p2 < p3:
                comp = nums[p2] + nums[p3]

                if comp > target:
                    p3 -= 1
                elif comp < target:
                    p2 += 1
                else:
                    res.append([-target, nums[p2], nums[p3]])
                    p2 += 1
                    
                    while nums[p2] == nums[p2 - 1] and p2 < p3:
                        p2 += 1
            
        return res
        