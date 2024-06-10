class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        lid=[]
        if a>b:
            for i in range(1,b+1):
                if a%i==0 and b%i==0:
                    lid.append(i)
        else:
            for i in range(1,a+1):
                if a%i==0 and b%i==0:
                    lid.append(i)
        return len(lid)
                
obj=Solution()
a=int(input("enter a value:"))
b=int(input("enter b value:"))
res=obj.commonFactors(a,b)
