class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        l=[]
        c=0
        for j in words:
            for k in range(len(j)):
                for i in allowed:
                    if i==j[k]:
                        l.append(i)
                if len(j)==len(l):
                    c+=1
            l.clear()
        print(c)

'''
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        a = set(allowed)
        for w in words:
            if set(w).issubset(a):
                res+=1
        return res
'''
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
obj = Solution()
obj.countConsistentStrings(allowed,words)