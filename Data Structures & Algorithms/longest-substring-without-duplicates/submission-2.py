class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        res = 0

        l = 0

        # "zxyzxyz"

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
                
            chars.add(s[r])
            res = max(res, r - l + 1)

        return res


