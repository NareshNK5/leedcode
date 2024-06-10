# 746. Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        c=0
        i=0
        if len(cost)<=3:
            return min(cost[-1],cost[-2])
        else:
            while i<len(cost)-1:
                if cost[i]<cost[i+1] and cost[i]!=0 and cost[i+1]!=0:
                    c+=min(cost[i],cost[i+1])
                    i+=2
                    print("c",c)
                else:
                    c+=min(cost[i],cost[i+1])
                    i+=1
                    print("c",c)

obj = Solution()
cost = [0,1,1,1]
obj.minCostClimbingStairs(cost)