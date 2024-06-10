class Solution(object):
    def threeSumClosest(self, nums, target):
        add=0
        l=len(nums)
        t=target
        for i in range(0,t):
            add=nums[i]+add
            if target==add:
                add=nums[i]+add
                print("test1",add)
                break
            elif target==(add+1):
                add=nums[i]+add
                print("test2",add)
                break
            elif target==(add-1):
                print("test3",add)
                break
            else:
                pass
        return add

#nums = [-1,2,1,-4]
#nums = [1,1,1,1]
nums=[0,1,2,3,4,5]
target = 2
obj=Solution()
obj.threeSumClosest(nums, target)
