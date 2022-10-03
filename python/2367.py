class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        ans += 1
        return ans
