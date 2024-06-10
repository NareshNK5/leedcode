class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        a=""
        for i in words:
            a+=i[0]
        if a==s:
            print(True)
        else:
            print(False)
'''
        a=""
        for i in words:
            a+=i[0]
        return a==s
'''
words = ["never","gonna","give","up","on","you"]
s = "ngguoy"
obj = Solution()
obj.isAcronym(words,s)