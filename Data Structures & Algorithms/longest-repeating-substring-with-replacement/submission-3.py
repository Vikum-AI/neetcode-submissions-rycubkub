class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 1
        max_len = 0

        hash_map = defaultdict(int)

        l = 0

        for i, c in enumerate(s):
            hash_map[c] += 1
            max_freq = max(max_freq, hash_map[c])

            substring_len = i - l + 1
            replacements = substring_len - max_freq

            while replacements > k:
                hash_map[s[l]] -= 1
                l += 1
                max_freq = max(hash_map.values())
                
                substring_len = i - l + 1
                replacements = substring_len - max_freq

            max_len = max(max_len, i - l + 1)

        return max_len



