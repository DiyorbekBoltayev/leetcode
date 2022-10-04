class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(0, n, 2):
            for j in range(0, n - i):
                ans += sum(arr[j:j + i + 1])

        return ans