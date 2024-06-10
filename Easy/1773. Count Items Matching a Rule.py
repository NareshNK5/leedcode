class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        cont = 0
        if ruleKey == "type":
            i=0
        elif ruleKey == "color":
            i=1
        else:
            i=2
        for j in range(len(items)):
            if items[j][i] == ruleValue:
                cont += 1
        print(cont)
        return cont
    
'''
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dic = {"type": 0, "color": 1, "name": 2 }
        ans = 0

        for item in items:
            if item[dic[ruleKey]] == ruleValue:
                ans += 1

        return ans
'''
items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
obj=Solution()
obj.countMatches(items,ruleKey,ruleValue)