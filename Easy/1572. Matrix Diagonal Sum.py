class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        l=0
        for i in range(len(mat)):
            for j in range(i+1):
                if i==j:
                    print(i,j)
                    l+=mat[i][j]
                for k in range(len(mat),-1,-1):
                    if i==j!=k and i+k==len(mat)-1:
                        print(k,j)
                        l+=mat[k][j]
        print(l)

'''
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = sum(mat[row][row] + mat[row][len(mat) - row - 1] for row in range(len(mat)))
        return res - mat[len(mat) // 2][len(mat) // 2] if len(mat) % 2 else res
'''
mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
obj = Solution()
obj.diagonalSum(mat)