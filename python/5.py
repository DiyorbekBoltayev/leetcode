class Solution:
    def isPolindrom(s: str) -> bool:
        if (s == s[::-1]):
            return True
        return False

    def longestPalindrome(self, s: str) -> str:
        n=len(s)-1
        for i in range(n,1,-1):
            j=0
            while j+i<n+1:
                a=3



        return 1



