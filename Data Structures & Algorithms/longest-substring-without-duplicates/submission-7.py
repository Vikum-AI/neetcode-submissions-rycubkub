class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        max_len = 1
        l, r = 0, 0

        seen = set(s[l])

        while r < len(s) - 1:
            while s[r+1] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r+1])
            r += 1

            sub_len = (r - l) + 1
            max_len = max(max_len, sub_len)

        return max_len
