class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        sum = 0
        res = []
        for candy in candies:
            sum = candy + extraCandies
            if sum >= max(candies):
                res.append(True)
            else:
                res.append(False)
                
        return res