from math import gcd
class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        count=0
        new_list=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] % 10 != 0 and nums[i]!=nums[j]:
                    lis=[]
                    lis.append(nums[i])
                    lis.append(nums[j])
                    new_list.append(lis)
                    count+=1
                    print(new_list)
        print(count)
                
obj=Solution()
nums=[31,25,72,79,74]
obj.countBeautifulPairs(nums)
