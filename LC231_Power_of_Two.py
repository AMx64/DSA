class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        log_n = log2(n)
        return log_n.is_integer()
        