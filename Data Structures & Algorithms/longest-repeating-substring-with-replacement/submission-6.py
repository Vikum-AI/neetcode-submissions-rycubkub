class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = defaultdict(int)

        res = 0
        max_res = 0

        for r in range(len(s)):
            counts[s[r]] += 1

            most_occ = 0

            for key, value in counts.items():
                most_occ = max(most_occ, value)

            while (r - l + 1) - most_occ > k:
                counts[s[l]] -= 1
                l += 1
                res -= 1

                for key, value in counts.items():
                    most_occ = max(most_occ, value)

            res += 1
            max_res = max(max_res, res)

        return max_res

                


        
            

