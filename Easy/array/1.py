#sum of two

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=nums1+nums2
        nums.sort()
        print(nums)
        print(len(nums))
        if (len(nums))%2==1:
            print("odd")
            x=int((len(nums))/2)
            print(nums[x])
            
        else:
            print("even")
            x=int((len(nums))/2)
            y=(nums[x]+nums[x-1])/2
            print(y)

nums1=[1,2]
nums2=[3,4]
obj=Solution()
obj.findMedianSortedArrays( nums1, nums2)
