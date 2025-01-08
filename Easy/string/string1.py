'''
nums=[1,2,1]
nums2=[]
for i in nums:
    print(i)
    nums2.append(i)
print(nums)
    
nums3=nums+nums2
print(nums3)
'''
class Solution():
    def getConcatenation(self,nums):
        # nums1=[]
        # nums2=[]
        
        # for i in nums:
        #     nums1.append(i)
        #     nums2 = nums + nums1
        #     print(nums2)
        # return nums2
        
        # num3=nums
        print(nums+nums)
        

nums=[1,2,1]
obj=Solution()
nums=obj.getConcatenation(nums)


