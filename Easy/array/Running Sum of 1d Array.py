class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        num=0
        lis=[]
        for i in range(len(nums)):
            num+=nums[i]
            lis.append(num)
        return lis
            
                
        
obj=Solution()
nums = [1,1,1,1,1]
obj.runningSum(nums)
