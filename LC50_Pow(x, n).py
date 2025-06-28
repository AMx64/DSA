class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(x, n):
            if n == 0:
                return 1
            half = fast_pow(x, n // 2)
            return half * half if n % 2 == 0 else half * half * x

        if n >= 0:
            return fast_pow(x, n)
        else:
            return 1 / fast_pow(x, -n)
