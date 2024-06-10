class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        flag=False
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                print("------------------------")
                print(i,j)
                if i!=j:
                    print(abs(i-j),indexDiff)
                    if abs(i-j)<=indexDiff:
                        print(abs(nums[i]-nums[j]) , valueDiff)
                        if abs(nums[i]-nums[j])<=valueDiff:
                            flag = True
                            break
        # return flag
        print(flag)
        
        
obj = Solution()
# nums = [1,2,3,1]
# indexDiff=3
# valueDiff=0

nums = [1,5,9,1,5,9]
indexDiff = 2
valueDiff = 3
obj.containsNearbyAlmostDuplicate(nums,indexDiff,valueDiff)