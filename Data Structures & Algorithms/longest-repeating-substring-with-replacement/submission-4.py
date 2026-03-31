class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 1
        max_len = 0

        hash_map = defaultdict(int)

        l = 0

        for i, c in enumerate(s):
            hash_map[c] += 1
            max_freq = max(max_freq, hash_map[c])

            while (i - l + 1) - max_freq > k:
                hash_map[s[l]] -= 1
                l += 1
                

            max_len = max(max_len, i - l + 1)

        return max_len



