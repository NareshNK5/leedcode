class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i<j<k:
                        if nums[j]-nums[i] == diff and nums[k]-nums[j]==diff:
                            count+=1
        print(count)

'''
class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i<j<k:
                        if nums[j]-nums[i] == diff and nums[k]-nums[j]==diff:
                            count+=1
        return count

        
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set()
        cnt = 0
        for num in nums:
            if num - diff in seen and num - diff * 2 in seen:
                cnt += 1
            seen.add(num)
        return cnt
'''
nums = [4,5,6,7,8,9]
diff = 2
obj=Solution()
obj.arithmeticTriplets(nums,diff)