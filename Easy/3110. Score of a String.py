# 3110. Score of a String

# print(ord("a"))

class Solution:
    def scoreOfString(self, s: str) -> int:
        r=0
        for i in range(len(s)-1):
            r+=abs(ord(s[i])-ord(s[i+1]))
        print(r)

'''

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i])-ord(s[i+1])) for i in range(len(s)-1))

'''


obj = Solution()
s="zaz"
obj.scoreOfString(s)