class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if len(set(s[i:j])) == len(s[i:j]):
                    ans = max(ans,j-i)
        return ans