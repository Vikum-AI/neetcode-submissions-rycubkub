from copy import deepcopy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_map = defaultdict(int)

        for char in s1:
            hash_map[char] += 1

        l = 0
        cond = len(hash_map.keys())
        hash_map_copy = deepcopy(hash_map)

        for r in range(len(s2)):
            c = s2[r]

            if c in hash_map:
                print(r, c, hash_map, cond)
                hash_map[c] -= 1

                if hash_map[c] == 0:
                    cond -= 1

                    if cond == 0:
                        return True

                while hash_map[c] < 0:
                    left_char = s2[l]

                    if left_char not in hash_map:
                        l += 1
                        continue

                    if hash_map[left_char] == 0:
                        cond += 1

                    hash_map[left_char] += 1
                    l += 1

            else:
                hash_map = deepcopy(hash_map_copy)
                print('hash', hash_map)
                cond = len(hash_map)
                l += 1

        return False


                

                