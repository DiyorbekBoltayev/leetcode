class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        ans = [first]
        for i in encoded:
            ans.append(ans[-1] ^ i)
        return ans

