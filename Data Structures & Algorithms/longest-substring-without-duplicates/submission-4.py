class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()

        l = 0

        local_len = 0
        max_len = 0

        for c in s:
            while c in substring:
                substring.remove(s[l])
                l += 1
                local_len -= 1

            substring.add(c)
            local_len += 1

            max_len = max(max_len, local_len)

        return max_len

        