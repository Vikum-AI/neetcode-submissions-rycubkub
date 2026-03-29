from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1

            hash_map[tuple(count)].append(s)


        return list(hash_map.values())
