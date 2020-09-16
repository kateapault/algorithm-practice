class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []
        maxCandies = max(candies)
        for val in candies:
            out.append(val + extraCandies >= maxCandies)
        return out