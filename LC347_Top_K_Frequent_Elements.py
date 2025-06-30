from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums_freq = Counter(nums)
        k_most_common = nums_freq.most_common(k)
        return [x[0] for x in k_most_common]