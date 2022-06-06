from typing import List, Optional

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        
        sortedByX = sorted(intervals, key=lambda x: x[0])
        merged = []
        for interval in sortedByX:
            if not merged:
                merged.append(interval)
                continue
            x, y = interval
            lastX, lastY = merged[-1]
            if x <= lastY:
                merged[-1] = [lastX, max(y, lastY)]
            else:
                merged.append(interval)
                
        return merged
    
s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
            