class Solution:
    seperator = '#'

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            res += f'{len(s)}{self.seperator}{s}'

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        l = 0
        r = 0

        while r < len(s):
            print(res, l, r)
            char_count = s[r]
            r += 1
            
            while s[r] != self.seperator:
                char_count += s[r]
                r += 1

            l = r + 2
            r += 1 + int(char_count)

            res.append(s[l-1:r])

            l = r

        return res


