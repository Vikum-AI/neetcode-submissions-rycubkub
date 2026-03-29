from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = defaultdict(int)

        for c in s:
            hash_map[c] += 1

        for c in t:
            hash_map[c] -= 1

        for value in hash_map.values():
            if value != 0:
                return False

        return True