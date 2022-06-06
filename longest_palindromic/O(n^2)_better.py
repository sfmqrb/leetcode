# O(n^2)
from pprint import pprint
class Solution:
    def longestPalindrome(self, s: str):
        # split the string in every character
        self.s = s
        self.max_len = 1
        self.max_substring = (0, 1)
        self.dp = [[-1] * len(self.s) for _ in range(len(self.s))]
        # base condition
        for i in range(len(self.s) - 1):
            self.dp[i][i] = 1
            if self.s[i] == self.s[i+1]:
                self.dp[i][i+1] = 2  
                self.update_max(i, 1)
            else:
                self.dp[i][i+1] = -1
        self.dp[len(self.s) - 1][len(self.s) - 1] = 1

        # dp enhancement
        for k in range(1, len(self.s)):
            for i in range(len(self.s) - k):
                if i + k - 1 >= i + 1 and self.dp[i + 1][i + k - 1] != -1:
                    if self.s[i] == self.s[i + k]:
                        self.dp[i][i + k] = self.dp[i + 1][i + k - 1] + 2
                        self.update_max(i, k)
                    else:
                        self.dp[i][i + k] = -1
                    
    
                        
        # pprint(self.dp, indent=4)  
        return self.s[self.max_substring[0]:self.max_substring[1]]

    def update_max(self, i, k):
        if self.dp[i][i + k] > self.max_len:
            self.max_len = self.dp[i][i + k]
            self.max_substring = (i, i + k + 1)
    
    
s = Solution()
print(s.longestPalindrome("xabax"))