class Solution:
    def fib(self, n: int) -> int:
        num=[0,1]
        if n<=0:
            return 0
        while len(num)<n:
            num.append(num[-1]+num[-2])
        return num[-1]+num[-2]
        # print(num)
            
            
            
        
        
obj = Solution()
n=3
obj.fib(n)