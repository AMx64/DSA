class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        right = nums[n-k:]
        left = nums[:n-k]
        nums.clear()
        nums.extend(right)
        nums.extend(left)