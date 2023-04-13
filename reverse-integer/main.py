class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = s[::-1]
        if s[-1] == '-':
            s = '-' + s[:-1]
        newx = int(s)

        zeroCond = True if newx < 2**31 and newx >= -2**31 else False

        return 0 if not zeroCond else newx
