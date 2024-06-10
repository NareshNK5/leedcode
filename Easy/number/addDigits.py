class Solution:
    def addDigits(self, num: int) -> int:
        st=str(num)
        le=len(st)
        res=0
        if le==1:
            return int(st)
        else:
            for i in range(0,le):
                res+=int(st[i])
            return obj.addDigits(res)

obj=Solution()
num=100
obj.addDigits(num)
print(obj.addDigits(num))
