class Solution:
    def get_digits_sum(self, digits_list):
        digits_sum = 0

        for digit in digits_list:
            digits_sum += pow(digit, 2)

        return digits_sum

    def isHappy(self, n: int) -> bool:
        nums = set()
        current_digits = n

        while True:
            digits = [int(d) for d in str(current_digits)]
            digits_sum = self.get_digits_sum(digits)

            print(digits, digits_sum)

            if digits_sum == 1:
                return True

            if digits_sum in nums:
                return False

            nums.add(digits_sum)
            current_digits = digits_sum