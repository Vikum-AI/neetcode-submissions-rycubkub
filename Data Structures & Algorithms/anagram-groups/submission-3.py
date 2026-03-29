

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for c in s:
                i = ord('a') - ord(c)
                counts[i] += 1

            hash_map[tuple(counts)].append(s)

        return list(hash_map.values())