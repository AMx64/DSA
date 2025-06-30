from collections import Counter

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        i = 1
        count = Counter(nums)
        while(True):
            if count.get(i) == 0 or count.get(i) == None:
                return i
            i += 1