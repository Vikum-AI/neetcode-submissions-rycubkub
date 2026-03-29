from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = defaultdict(int)

        l = 0
        res = 0

        for r in range(len(s)):
            c = s[r]
            hash_map[c] += 1

            while (r - l + 1) - max(hash_map.values()) > k:
                left_char = s[l]
                
                hash_map[left_char] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
