class Solution:
    def isPalindrome(self, x: int) -> bool:
        abs_x = abs(x)
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False

        #original = x
        #if x < 0:
        #   return False
        #reversed_x = 0
        #while x>0:
        #   reversed_x = reversed_x*10 + x%10
        #   x = x // 10
        #if original == reversed_x:
        #   return True
        #else:
        #   return False