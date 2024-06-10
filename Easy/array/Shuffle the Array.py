class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        num1=[]
        for i in range(len(nums)):
            for i in range(i,len(nums),n):
                num1.append(nums[i])
                if len(num1)==len(nums):
                    print(num1)
                    return num1

obj=Solution()
nums=[1,2,3,4,4,3,2,1]
n = 4
obj.shuffle(nums,n)
