from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for i, s in enumerate(strs):
            s_sorted = tuple(sorted(s))
            hash_map[s_sorted].append(s)

        res = []
        
        for key, val in hash_map.items():
            res.append(val)

        return res