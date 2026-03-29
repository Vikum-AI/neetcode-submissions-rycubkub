class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''

        max_len = 1
        max_pal = s[0]

        for i in range(len(s)):
            # odd case
            l, r = i - 1, i + 1
            length = 1
            cur_pal = s[i]

            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 2
                cur_pal = s[l] + cur_pal + s[r]

                if length > max_len:
                    max_len = length
                    max_pal = cur_pal

                r += 1
                l -= 1

                
            l, r = i, i + 1
            length = 0
            cur_pal = ''

            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 2
                cur_pal = s[l] + cur_pal + s[r]

                if length > max_len:
                    max_len = length
                    max_pal = cur_pal

                r += 1
                l -= 1
        

        return max_pal

