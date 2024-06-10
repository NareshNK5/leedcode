class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        count=0
        for i in hours:
            if i>=target:
                count+=1
        print(count)
obj=Solution()
hours = [0,1,2,3,4]
target = 2
obj.numberOfEmployeesWhoMetTarget(hours,target)
