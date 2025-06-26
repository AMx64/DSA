class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(2, n+2):
            a, b = b, a+b
        return b
