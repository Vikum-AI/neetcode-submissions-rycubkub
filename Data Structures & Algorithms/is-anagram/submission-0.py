from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = defaultdict(int)

        for char in s:
            hash_map[char] += 1

        for char in t:
            hash_map[char] -= 1

        for val in hash_map.values():
            if val != 0:
                return False

        return True
