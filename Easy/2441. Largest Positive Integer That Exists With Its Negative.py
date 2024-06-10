# 2441. Largest Positive Integer That Exists With Its Negative

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        lis = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i]) == abs(nums[j]):
                    if nums[i]<0 and nums[j]>0 or nums[i]>0 and nums[j]<0:
                        lis.append(nums[i])
        if len(lis)==0:
            print(-1) 
        print(max(lis))
        
        
        lis = max([abs(nums[i]) for i in range(len(nums)-1) for j in range(i+1,len(nums)) if abs(nums[i]) == abs(nums[j])])
        # print(lis)
        
        '''
        class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        li=[]
        for i in nums:
            if i<0 and abs(i) in nums:
                li.append(abs(i))
        if len(li)==0:
            return -1 
        else:
            return max(li)
        
        '''
nums = [-9,-43,24,-23,-16,-30,-38,-30]
obj = Solution()
obj.findMaxK(nums)