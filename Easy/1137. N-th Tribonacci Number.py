class Solution(object):
    def tribonacci(self, n):
        if n<2:
            return n
        d=[0,1,1]
        for i in range(3,n+1):
            d[0],d[1],d[2]=d[1],d[2],sum(d)
        print(d[2])
obj = Solution()
n=25
obj.tribonacci(n)

'''
class Solution:
  def tribonacci(self, n: int) -> int:
    dp = [0, 1, 1]

    for i in range(3, n + 1):
      dp[i % 3] = sum(dp)

    return dp[n % 3]
'''

'''
class Solution:
  def tribonacci(self, n: int) -> int:
    if n < 2:
      return n

    dp = [0, 1, 1]

    for _ in range(3, n + 1):
      dp[0], dp[1], dp[2] = dp[1], dp[2], sum(dp)

    return dp[2]
'''

'''
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [0, 1, 1]
        if n < 3:
            return T[n]

        for i in range(3, n+1):
            T.append(sum(T[i-3:i]))
        return T[-1]
'''