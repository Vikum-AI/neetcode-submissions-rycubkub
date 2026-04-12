class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][0]:
                value, j = stack.pop()
                res[j] = i - j

            stack.append((tmp, i))

        return res

