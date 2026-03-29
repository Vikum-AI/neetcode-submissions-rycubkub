class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = defaultdict(int)

        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            value = target - num
            if value in nums_map.keys():
                if nums_map[value] == i:
                    continue
                return [i, nums_map[value]]

        return [-1, -1]