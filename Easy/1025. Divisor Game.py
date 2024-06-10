# 1025. Divisor Game
class Solution:
    def divisorGame(self, n: int) -> bool:
        if (n%2==0):
            return True
        else:
            return False

# class Solution:
#     def divisorGame(self, n: int) -> bool:
#         return n % 2==0
    
    
obj=Solution()
n=2
obj.divisorGame(n)