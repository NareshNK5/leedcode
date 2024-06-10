class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        a=0
        for i in nums:
            i=str(i).split(" ")
            for j in i:
                if len(j)%2==0:
                    a+=1
        print(a)
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([num for num in nums if len(str(num)) % 2 == 0])
'''
nums = [555,901,482,1771]
obj=Solution()
obj.findNumbers(nums)