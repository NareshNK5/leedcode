# 2769. Find the Maximum Achievable Number

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num+(t*2)
    

obj = Solution()
num = 3
t = 2
obj.theMaximumAchievableX(num,t)