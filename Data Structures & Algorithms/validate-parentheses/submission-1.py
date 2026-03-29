class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        opening_brackets = ['(', '{', '[']
        closing_brackets = [')', '}', ']']

        stack = []

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if len(stack) < 1:
                    return False

                value = stack.pop()
                
                if value != hash_map[char]:
                    return False
            else:
                return False

            
        return len(stack) == 0

