import string
class Solution:
    def toLowerCase(self, s: str) -> str:
        print(s)
        ns=""
        al = string.ascii_lowercase
        for i in range(len(s)):
            for j in al:
                if not s[i].lower()!=j:
                    print("test",s[i],j)
        print("result",s)
s = "al&phaBET"
obj = Solution()
obj.toLowerCase(s)