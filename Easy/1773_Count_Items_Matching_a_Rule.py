# 1773. Count Items Matching a Rule

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0

        if ruleKey == "type":
            for i in items:
                if i[0] == ruleValue:
                    ans+=1
                continue

        elif ruleKey == "color":
            for i in items:
                if i[1] == ruleValue:
                    ans+=1
                continue

        else:
            for i in items:
                if i[2] == ruleValue:
                    ans+=1
                continue

        return ans