import re
class Solution:
    def myAtoi(self, s: str) -> int:
        ls = re.findall(
            r'^[-+]?\d+', 
            s.strip()
        )
        if not ls:
            return 0
        to_return = int(ls[0])
        if to_return > 2**31 - 1:
            return 2**31 - 1
        elif to_return < -2**31:
            return -2**31
        return to_return
        

        
s = Solution()
print(s.myAtoi('   +723dfsd32'))