#Split a String in Balanced Strings
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s)
        count=1
        for i in range(len(s)):
            if s[i]=="R" and s[i+1]=="L":
                count+=1
        print(count)
obj=Solution()
s = "RLRRRLLRLL"
obj.balancedStringSplit(s)
