class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_pos_map = []
        group_map = defaultdict(list)

        for s in strs:
            char_pos_list = [0] * 26
            
            for c in s:
                value = ord(c) - ord('a')
                char_pos_list[value] += 1

            key = tuple(char_pos_list)

            group_map[key].append(s)

        return list(group_map.values())