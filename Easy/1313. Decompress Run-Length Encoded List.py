class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        #print(nums)
        a=[]
        for i in range(0,len(nums),2):
            for j in range(nums[i]):
                a.append(nums[i+1])
        print(a)
        return a

'''
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        for num_occurrences, digit in zip(*[iter(nums)] * 2):
            yield from repeat(digit, num_occurrences)
'''
nums = [1,1,2,3]
obj=Solution()
obj.decompressRLElist(nums)
