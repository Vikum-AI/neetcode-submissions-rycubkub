class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            value = hash_map.get(diff)

            if value is not None:
                return [value, i]

            hash_map[num] = i


        return [-1, -1]