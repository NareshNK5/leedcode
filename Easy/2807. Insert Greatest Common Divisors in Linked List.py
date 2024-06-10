class Solution:
    def insertGreatestCommonDivisors(self,head):
        res=[]
        for i in range(len(head)-1):
            def gcd(a,b):
                if(b==0):
                    return abs(a)
                else:
                    return gcd(b,(a%b))
            n = gcd(head[i],head[i+1])
            res.append(head[i])
            res.append(n)
        res.append(head[-1])
        print(res)
obj = Solution()
head = [18,6,10,3]
obj.insertGreatestCommonDivisors(head)