class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]-nums[j]==k:
                    count+=1
        print(count)
nums = [3,2,1,5,4]
k = 2
obj = Solution()
obj.countKDifference(nums,k)