class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        s = 0
        for i in range(len(nums)):
            n = nums[i:].count(nums[i])
            m = nums[:i].count(nums[i])
            s += int((n * (n - 1)) / 2)
            s -= int((m * (m - 1)) / 2)
        return s
