class Solution:
    def lengthOfLongestSubstring(self, s: str):
        i, j = 0, 0
        if len(s) > 0:
            set_of_unique_chars = set(s[0])
            self.max_len = 1
        else:
            self.max_len = 0
            return self.max_len
        while i < len(s):
            incoming_j = s[-1] if j >= len(s) - 1 else s[j+1]

            if incoming_j in set_of_unique_chars:
                self.update_max_len(i, j)
                set_of_unique_chars.remove(s[i])
                i += 1
            else:
                j += 1
                set_of_unique_chars.add(s[j])

        return self.max_len

    def update_max_len(self, i, j):
        l = j - i + 1
        self.max_len = l if l > self.max_len else self.max_len


s = Solution()
print(s.lengthOfLongestSubstring("abcddabcbb"))
