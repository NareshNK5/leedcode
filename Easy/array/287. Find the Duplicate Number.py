'''
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
      
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i!=j and i>j:
                    #return nums[i]
                    print(nums[i])

    
obj=Solution()
nums= [3,1,3,4,2]
obj.findDuplicate(nums)

'''
class Solution:
    """ 287. Find the Duplicate Number """

    def findDuplicate(self, nums: list[int]) -> int:
        """ O(N)T O(1)S """
        slow1, fast1, slow2, result = nums[0], nums[nums[0]], 0, None
                                    #3,num[3] 4,0
        # (a) find cycle
        while slow1 != fast1:#3!=4
            DEBUG = slow1, slow2#3,0
            slow1 = nums[slow1]#nums[3]=4
            fast1 = nums[nums[fast1]]#nums[nums[fast1]]=nums[nums[4]]=nums[2]=3

        # (b) find cycle start
        while slow1 != slow2:
            slow1 = nums[slow1]#nums[3]=4
            slow2 = nums[slow2]#nums[0]=3
        print(slow2)
        return slow2

obj=Solution()
nums= [3,1,3,4,2]
obj.findDuplicate(nums)
