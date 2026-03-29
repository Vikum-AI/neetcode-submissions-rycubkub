from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counts = defaultdict(int)

        for c in s:
            char_counts[c] += 1

        for c in t:
            char_counts[c] -= 1

        for val in char_counts.values():
            if val != 0:
                return False

        return True