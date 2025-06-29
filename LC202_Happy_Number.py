class Solution:
    def isHappy(self, n: int) -> bool:
        n_set = set()
        while n != 1 and n not in n_set:
            n_set.add(n)
            n = sum(int(char) ** 2 for char in str(n))
        return n == 1
       