class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        print(nums,target)
        count=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                diff=nums[i]+nums[j]
                print(diff,target)
                if i<j and diff < target:
                    count+=1
        print("count",count)
        return count
obj=Solution()
nums = [-1,1,2,3,1]
target = 2
obj.countPairs(nums,target)
