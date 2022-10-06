class Solution:
    def romanToInt(self, s: str) -> int:
        rim = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i + 1 < len(s) and rim[s[i]] < rim[s[i + 1]]:
                ans -= rim[s[i]]
            else:
                ans += rim[s[i]]
        return ans
