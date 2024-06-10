class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        lis=[]
        for i in range(len(nums)):
            lis.append(nums[nums[i]])
        print(lis)
obj=Solution()
nums = [5,0,1,2,3,4]
obj.buildArray(nums)
