class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        starting = set()

        elements = set(nums)

        for num in nums:
            if num-1 not in starting:
                cur_num = num
                cur_len = 1

                while cur_num+1 in elements:
                    cur_len += 1
                    cur_num += 1

                max_len = max(max_len, cur_len)
                starting.add(num)


        return max_len
            