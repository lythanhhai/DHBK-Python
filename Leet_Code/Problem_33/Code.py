import math
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        res = []
        for i in nums:
            if i == 1:
                max += 1
            else:
                res.append(max)
                max = 0
        if max > 0:
            res.append(max)
        Max = 0
        for i in res:
            if i > Max:
                Max = i
        return Max