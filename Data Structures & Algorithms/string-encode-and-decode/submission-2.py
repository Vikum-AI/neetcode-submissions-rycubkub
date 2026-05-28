class Solution:
    key = '#'

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            res += f'{len(s)}{self.key}{s}'

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        # 10#car2#it

        while r < len(s):
            while s[r+1] != self.key:
                r += 1
            print(s[l:r+1])
            count = int(s[l:r+1])

            word = s[r+2:count+r+2]
            res.append(word)

            r += count + 2
            l = r

        return res


