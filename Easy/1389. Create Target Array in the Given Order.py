class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        l=[]
        for i in range(len(nums)):
            l.insert(index[i],nums[i])
        return l

'''
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for n, i in zip(nums,index): 
            arr[i:i] = [n]
        return arr

'''

'''
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for (i, j) in zip(nums, index):
            target.insert(j, i)
        return target
'''
nums = [1]
index = [0]
obj=Solution()
obj.createTargetArray(nums,index)
