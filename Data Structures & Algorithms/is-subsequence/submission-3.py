class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        if s == "":
            return True
        
        for c in t:
            if i >= len(s):
                return True
            
            if s[i] == c:
                i += 1

        print(i)

        return i >= len(s)