# O(n^3)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.lleft = 0
        self.lright = 0
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_pal(s, i, j):
                    if j - i + 1 > self.lright - self.lleft + 1:
                        self.lleft, self.lright = i, j 
        return s[self.lleft:self.lright + 1]
                
    def is_pal(self, s, left=0, right=0):
        for i in range((right - left + 1)//2):
            if s[left + i] != s[right - i]:
                return False
        return True
    
    
s = Solution()
# print(s.is_pal("abaa", 0, 2))
print(s.longestPalindrome("lejyqjcpluiggwlmnumqpxljlcwdsirzwlygexejhvojztcztectzrepsvwssiixfmpbzshpilmojehqyqpzdylxptsbvkgatzdlzphohntysrbrcdgeaiypmaaqilthipjbckkfbxtkreohabrjpmelxidlwdajmkndsdbbaypcemrwlhwbwaljacijjmsaqembgtdcskejplifnuztlmvasbqcyzmvczpkimpbbwxdtviptzaenkbddaauyvqppagvqfpednnckooxzcpuudckakutqyknuqrxjgfdtsxsoztjkqvfvelrklforpjnrbvyyvxigjhkjmxcphjzzilvbjbvwiwnnkbmboiqamgoimujtswdqesighoxsprhnsceshotakvmoxqkqjvbpqucvafiuqwmrlfjpjijbctfupywkbawquchbclgvhxbanybret"))