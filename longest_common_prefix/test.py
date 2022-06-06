from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        common = strs[0]
        for el in strs:
            common = self.get_common(el, common)
        return common


    def get_common(self, s2, s1):
        ls = list(zip(s1, s2))
        count = 0
        for el in ls:
            if el[0] == el[1]:
                count += 1
            else:
                break
        return s1[:count]


s = Solution()
a = s.longestCommonPrefix(["follow", "folow", "foler"])
print(a)
