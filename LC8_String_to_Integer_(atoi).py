class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        ans, i = "", 0
        if s[0] == "-":
            ans = "-"
            i = 1
        elif s[0] == "+":
            i = 1

        while i < len(s) and s[i].isdigit():
            ans += s[i]
            i += 1

        if ans == "" or ans == "-":
            return 0

        num = int(ans)
        int_min, int_max = -2**31, 2**31 - 1

        if num < int_min:
            return int_min
        if num > int_max:
            return int_max
        return num