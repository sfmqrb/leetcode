class Solution:
    @staticmethod
    def _s3_idx(s1_idx, s2_idx): 
        return s1_idx + s2_idx

    def set_dp_cell(self, s1_idx, s2_idx, val):
        self.dp[s1_idx][s2_idx] = val

    def get_dp_cell(self, s1_idx, s2_idx):
        return self.dp[s1_idx][s2_idx]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        self.dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        
        # base condition
        for s1_idx in range(len(self.dp)):
            if s1_idx == 0:
                self.set_dp_cell(s1_idx, 0, True)
            else:
                self.set_dp_cell(s1_idx, 0, 
                                 self.get_dp_cell(s1_idx - 1, 0) 
                                 and s1[s1_idx - 1] == s3[s1_idx - 1])
        
        for s2_idx in range(len(self.dp[0])):
            if s2_idx == 0:
                self.set_dp_cell(0, s2_idx, True)
            else:
                self.set_dp_cell(0, s2_idx,
                                 self.get_dp_cell(0, s2_idx - 1)
                                 and s2[s2_idx - 1] == s3[s2_idx - 1])
        
        for s1_idx in range(1, len(self.dp)):
            for s2_idx in range(1, len(self.dp[0])):
                s3_idx = Solution._s3_idx(s1_idx, s2_idx)
                
                up_cond = self.get_dp_cell(s1_idx - 1, s2_idx) and s3[s3_idx - 1] == s1[s1_idx - 1]
                left_cond = self.get_dp_cell(s1_idx, s2_idx - 1) and s3[s3_idx - 1] == s2[s2_idx - 1]
                
                self.set_dp_cell(s1_idx, s2_idx,
                                 up_cond
                                 or left_cond)
                
        # from pprint import pprint
        # pprint(self.dp, indent=4, width=80, depth=None)
        
        return self.get_dp_cell(len(self.dp) - 1, len(self.dp[0]) - 1)


s = Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(s.isInterleave("", "b", "b"))
