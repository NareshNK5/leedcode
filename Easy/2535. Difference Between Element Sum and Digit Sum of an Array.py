class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        sum1=0
        sum2=0
        for i in nums:
            sum1+=i
        for i in nums:
            output = [int(x) for x in str(i)]
            sum2+=sum(output)
        return sum1-sum2


# class Solution:
#     def differenceOfSum(self, nums: list[int]) -> int:
        
        # digits = [int(digit) for num in nums for digit in str(num)]
        # print(digits)
        # return abs(sum(nums) - sum(digits))

nums = [1,15,6,3]
obj=Solution()
obj.differenceOfSum(nums)