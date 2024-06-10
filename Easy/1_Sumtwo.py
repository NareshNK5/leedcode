class Solution:
   def twoSum(self nums: list[int], target: int):
       seen = {}
       for i, value in enumerate(nums):
           remaining = target - nums[i]
           
           if remaining in seen:
               return [i, seen[remaining]]
            
           seen[value] = i
nums=[2,3,4,5,6,7]
target=9
s=Solution
s.twoSum(nums,target)
