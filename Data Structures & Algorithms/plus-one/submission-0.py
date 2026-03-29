class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_for = 0
        index = len(digits) - 1

        cond = len(digits) - 1

        res = []

        while index >= 0 or carry_for:
            val = 0

            if index >= 0:
                val = digits[index]

            if index == cond:
                val += 1
            
            val += carry_for
            carry_for = 0

            if val > 9:
                carry_for = val // 10 
                val = val % 10

            res.insert(0, val)
            index -= 1


        return res            