
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        check = []
        n = len(candyType)
        candyType = list(dict.fromkeys(candyType))
        return min(len(candyType), int(n / 2))
        