# O(n^2)
from pprint import pprint
class Solution:
    def longestPalindrome(self, s: str):
        # split the string in every character
        max_len = 0
        max_substring = ''
        new_s = ""
        for el in s:
            new_s += el + "#"
        s = new_s[:-1]
        self.dp = [[None] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            self.dp[i][i] = 1
        for k in range(1, len(s)):
            for i in range(len(s) - k):
                if i + k - 1 >= i + 1 and self.dp[i + 1][i + k - 1] is not None:
                    self.dp[i][i + k] = self.dp[i + 1][i + k - 1] + 2 if\
                        s[i] == s[i + k] else None
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.dp[i][j] is not None:
                    if s[i] == '#':
                        self.dp[i][j] //= 2
                    else:
                        self.dp[i][j] += 1
                        self.dp[i][j] //= 2
                    if self.dp[i][j] > max_len:
                        max_len = self.dp[i][j]
                        max_substring = s[i:j + 1]
                        
        # pprint(self.dp, indent=4)  
        return max_substring.replace('#', '')
                        
        
        # return 
                
    def is_pal(self, s, left=0, right=0):
        for i in range((right - left + 1)//2):
            if s[left + i] != s[right - i]:
                return False
        return True
    
    
s = Solution()
# print(s.is_pal("abaa", 0, 2))
print(s.longestPalindrome("lejyqjcpluiggwlmnumqpxljlcwdsirzwlygexejhvojztcztectzrepsvwssiixfmpbzshpilmojehqyqpzdylxptsbvkgatzdlzphohntysrbrcdgeaiypmaaqilthipjbckkfbxtkreohabrjpmelxidlwdajmkndsdbbaypcemrwlhwbwaljacijjmsaqembgtdcskejplifnuztlmvasbqcyzmvczpkimpbbwxdtviptzaenkbddaauyvqppagvqfpednnckooxzcpuudckakutqyknuqrxjgfdtsxsoztjkqvfvelrklforpjnrbvyyvxigjhkjmxcphjzzilvbjbvwiwnnkbmboiqamgoimujtswdqesighoxsprhnsceshotakvmoxqkqjvbpqucvafiuqwmrlfjpjijbctfupywkbawquchbclgvhxbanybret"))