class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = 0
        for i in range(len(digits)):
            number += digits[i] * (10**(len(digits)-i-1))
        number += 1

        return [int(x) for x in str(number)]