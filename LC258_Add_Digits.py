class Solution:
    def add(self, num):
        num_list = [int(char) for char in str(num)]
        return sum(num_list)

    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = self.add(num)
        return num