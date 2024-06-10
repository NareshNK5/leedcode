class Solution:
    def sumOfMultiples(self, n: int) -> int:
        lis=[]
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                lis.append(i)
        if n<3:
            return 0
        elif n==4:
            return sum(lis)
        else:
            return sum(lis)
                


obj=Solution()
n=int(input("enter number:"))
print(obj.sumOfMultiples(n))
