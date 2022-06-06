class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1
        res = 0
        for i in s:
            if i.isdigit():
                res = res * 10 + int(i)
            else:
                break
        res = sign * res
        if res > 2**31 - 1:
            return 2**31 - 1
        elif res < -2**31:
            return -2**31
        else:
            return res
        
s = Solution()
print(s.myAtoi('-72332'))