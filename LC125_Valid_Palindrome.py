class Solution:
    def isPalindrome(self, s: str) -> bool:
        mod_str = []
        for char in s:
            if char.isalnum():
                mod_str.append(char.lower())
        return mod_str == mod_str[::-1]
