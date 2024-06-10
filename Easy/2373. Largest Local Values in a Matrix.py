class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        for i in range(len(grid)):
            for j in range(len(grid)-1):
                if grid[i][j] > grid[i][j+1]:
                    print(grid[i][j])
                    print(max(grid))
    
grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
obj = Solution()
obj.largestLocal(grid)