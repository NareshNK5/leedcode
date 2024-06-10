class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        print(nums)
        count=0
        for i in range(0,len(nums)-1):
            for j in range(i,len(nums)):
                if nums[i]==nums[j] and i!=j:
                    count+=1
        return count
obj=Solution()
nums = [1,1,1,1]
obj.numIdenticalPairs(nums)
