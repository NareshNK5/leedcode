# class Solution:
#     def generate(self, numRows: int) -> list[list[int]]:
#         lis = [[1]]
#         for i in range(numRows-1):
#             if numRows>=i:
#                 sunblis=[1,1]
#                 lis.append(sunblis)
#                 for j in range(i):
#                     print("***************",i)
#                     print(lis)
#                     print("b :",lis[-1])
#                     print(j,(j+1),lis[-2][j],lis[-2][j+1])
#                     lis[-1].insert((j+1),(lis[-1][j]+lis[-1][j+1]))
#                     print("a :",lis[-1])                
#                     print(lis)

#         print(lis)

class Solution:
  def generate(self, numRows: int) -> list[list[int]]:
    ans = []

    for i in range(numRows):
      ans.append([1] * (i + 1))

    for i in range(2, numRows):
      for j in range(1, len(ans[i]) - 1):
        ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        print(ans[i][j],ans[i - 1][j - 1] , ans[i - 1][j])

    print(ans) 
    # return ans
        
obj = Solution()
numRows=5
obj.generate(numRows)