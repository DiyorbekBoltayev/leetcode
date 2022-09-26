class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans = []
        maximum = max(candies)
        for i in candies:
            if ((i + extraCandies) >= maximum):
                ans.append(True)
            else:
                ans.append(False)
        return ans
