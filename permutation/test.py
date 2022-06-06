from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:        
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        l = []

        for i in range(len(nums)):
            m = nums[i]
            remLst = nums[:i] + nums[i+1:]
            for p in self.permute(remLst):
                l.append([m] + p)
        return l

s = Solution()
data = [1,2,3]
print(s.permute(data))
