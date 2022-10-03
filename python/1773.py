class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        ans = []
        for i in items:
            if ruleKey == 'type' and ruleValue == i[0] or ruleKey == 'color' and ruleValue == i[1] or ruleKey == 'name'\
                    and ruleValue == i[2]:
                ans.append(i)
        return len(ans)