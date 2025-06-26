class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return [index_map[complement], index]
            index_map[num] = index