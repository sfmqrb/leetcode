from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:        
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        l = []

        for i in range(len(nums)):
            m = nums[i]
            remLst = nums[:i] + nums[i+1:]
            for p in self.permuteUnique(remLst):
                l.append([m] + p)
        t = list(map(lambda ls: tuple(ls), l))
        new_t = set(t)
        new_l = list(map(lambda t: list(t), new_t))   
        return new_l
    
    
s = Solution()
print(s.permuteUnique([1,2,1]))