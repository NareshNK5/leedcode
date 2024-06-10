class Solution:
    def findGCD(self, nums: list[int]) -> int:
        #print(nums)
        lis=[]
        le=len(nums)
        snum=sorted(nums)
        print(snum)
        for num in range(1,(snum[0]+1)):
            if snum[0]%num==0 and snum[le-1]%num==0:
                lis.append(num)
        print(lis,lis[len(lis)-1])
        #return lis[len(lis)-1]
obj=Solution()
nums=[48,20,30,12,41]
obj.findGCD(nums)
