'''
class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        l=[]
        for i in range(len(nums)):
            a=bin(i)[2:]
            c=0
            for j in a:
                if j=='1':
                    c+=1
            if c==k:
                l.append(nums[i])
        return sum(l)
'''

'''
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s=0
        for i in range(len(nums)):
            a=bin(i)
            if a.count("1")==k:
                s+=nums[i]
        return s
'''

class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        res = 0
        print(enumerate(nums))
        for i, num in enumerate(nums):
            if i.bit_count() == k:
                res += num
        return res


nums = [5,10,1,5,2]
k = 1
obj=Solution()
obj.sumIndicesWithKSetBits(nums,k)
