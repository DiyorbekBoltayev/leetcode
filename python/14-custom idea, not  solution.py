
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans=''
        m = min(strs)
        index = strs.index(m)
        strs.pop(index)
        n = len(m)
        for i in range(n):
            for k in range(n - i):
                str_slice = m[k:k + i + 1]
                bl = False
                for j in strs:
                    if str_slice not in j:
                        bl = True
                        break

                if bl:
                    break
                else:
                    ans = str_slice

        return ans
