class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            if target - numbers[left] == numbers[right]:
                return [left+1, right+1]
            elif target - numbers[left] < numbers[right]:
                right -= 1
            elif target - numbers[left] > numbers[right]:
                left += 1
        