from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = defaultdict(int)

        for c in s:
            char_map[c] += 1

        for c in t:
            char_map[c] -= 1

        for key, val in char_map.items():
            if val != 0:
                return False

        return True