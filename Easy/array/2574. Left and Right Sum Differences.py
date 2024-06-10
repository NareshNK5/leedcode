class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        l=[]
        r=[]
        ll=0
        rr=0
        res=[]
        for i in nums:
            r.append(rr)
            rr+=i
        for j in range(len(nums)-1,-1,-1):
            l.insert(0,ll)
            ll+=nums[j]
        for k in range(len(nums)):
            res.append(abs(r[k]-l[k]))
        return res
        
nums = [10,4,8,3]
obj=Solution()
obj.leftRightDifference(nums)
