class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                l_str, r_str = s[l+1:r+1], s[l:r]

                return l_str == l_str[::-1] or r_str == r_str[::-1]

            l, r = l+1, r-1

        return True