class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        print(len(candies),max(candies))
        lis=[]
        for i in range(len(candies)):
            tot=candies[i]+extraCandies
            if tot>=max(candies):
                lis.append(True)
            else:
                lis.append(False)
        print(lis)
obj=Solution()
candies = [12,1,12]
extraCandies = 10
obj.kidsWithCandies(candies,extraCandies)
