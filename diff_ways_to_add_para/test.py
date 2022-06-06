from typing import List

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        res.append(eval(str(l) + input[i] + str(r)))
        return res
    
if __name__ == "__main__":
    s = Solution()
    l = s.diffWaysToCompute("2-1-1+10*3")
    print(l)