class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        res = [-1, -1]
        res_len = float('inf')

        need_map = defaultdict(int)
        
        for c in t:
            need_map[c] += 1

        need = len(need_map.keys())

        have = 0
        have_map = defaultdict(int)

        l = 0

        for r in range(len(s)):
            c = s[r]

            if c in need_map:
                have_map[c] += 1

                if need_map[c] == have_map[c]:
                    have += 1

                while need == have:
                    if (r - l + 1) < res_len:
                        res_len = r - l + 1
                        res = [l, r]

                    if s[l] in need_map:
                        have_map[s[l]] -= 1

                        if have_map[s[l]] < need_map[s[l]]:
                            have -= 1

                    l += 1
        
        start, end = res
        return s[start:end+1] if res_len != float('inf') else ""
            