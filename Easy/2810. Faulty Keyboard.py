class Solution:
    def finalString(self, s: str) -> str:
        ns=""
        for i in s:
            if i != "i":
                ns+=i
            else:
                ns=ns[::-1]
        return ns

s = "poiinter"
obj = Solution()
obj.finalString(s)