from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        size = len(nums)
        freq_map = Counter(nums)
        return freq_map.most_common(1)[0][0]      