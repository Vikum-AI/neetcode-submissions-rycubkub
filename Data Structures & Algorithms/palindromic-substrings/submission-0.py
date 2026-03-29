class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        
        # odd palindromes 
        for i in range(len(s)):
            l, r = i - 1, i + 1

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                l -= 1
                r += 1

                res += 1

        
        # even palindromes
        for i in range(len(s)):
            l, r = i, i + 1

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                l -= 1
                r += 1

                res += 1

        return res 


