
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans=''
        m = min(strs)
        index = strs.index(m)
        strs.pop(index)
        n = len(m)



        return ans
