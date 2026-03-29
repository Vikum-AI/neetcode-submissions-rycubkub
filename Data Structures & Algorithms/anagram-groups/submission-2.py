

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for s in strs:
            val_arr = [0] * 26

            for c in s:
                val = ord('a') - ord(c)
                val_arr[val] += 1

            hash_map[tuple(val_arr)].append(s)

        return list(hash_map.values())