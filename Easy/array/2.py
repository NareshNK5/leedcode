class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        x=0
        leg=(len(height))
        for i in range(1,leg):
            #print(i)
            x=height[i]+x
            #print(height[i])
            #print(x)
        return x
height = [1,8,6,2,5,4,8,3,7]
obj=Solution()
obj.maxArea(height)
