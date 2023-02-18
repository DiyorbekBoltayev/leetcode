class Solution:
    def isValid(self, s: str) -> bool:
        open_q = ['(', '{', '[']
        close_q = [')', '}', ']']
        t = []
        for i in s:
            if i in open_q:
                t.append(i)
            else:
                if len(t) == 0 :
                    return False
                index = close_q.index(i)
                if t[-1] != open_q[index]:
                    return False
                else:
                    t.pop()

        if len(t) == 0:
            return True
        else:
            return False


print(Solution().isValid(']'))
