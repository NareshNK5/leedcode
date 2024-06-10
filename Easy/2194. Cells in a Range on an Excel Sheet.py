import string
class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        s=s.split(":")
        l=[]
        for i in string.ascii_uppercase:
            if  i >= s[0][0] and i <=s[1][0]:
                for j in range(int(s[0][1]),int(s[1][1])+1):
                    if  j >= int(s[0][1]) and j <=int(s[1][1]):
                        l.append(i+str(j))
        print(l)

'''
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res=[]
        for i in range(ord(s[0]), ord(s[3])+1):
            for j in range(int(s[1]), int(s[4])+1):
                res.append(chr(i)+str(j))
        return res
'''
        
s = "K1:L2"
obj = Solution()
obj.cellsInRange(s)