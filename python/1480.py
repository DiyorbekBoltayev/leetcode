class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.insert(i, sum(nums[0:i + 1]))
        return ans
