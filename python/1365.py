class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            n = 0
            for j in nums:
                if j < i: n += 1
            ans.append(n)
        return ans
