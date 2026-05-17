class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for c in s:
            if c in bracket_map.keys():
                stack.append(c)
            else:
                if len(stack) <= 0:
                    return False

                key = stack.pop()

                if bracket_map[key] != c:
                    return False


        return len(stack) == 0
