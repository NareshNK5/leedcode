# 2418. Sort the People

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if(heights[i]<heights[j]):
                    heights[j],heights[i]=heights[i],heights[j]
                    names[j],names[i]=names[i],names[j]
        return names
        
names = ["Mary","John","Emma"]
heights = [180,165,170]
obj = Solution()
obj.sortPeople(names,heights)