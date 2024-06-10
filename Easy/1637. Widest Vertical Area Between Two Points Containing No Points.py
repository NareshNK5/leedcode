import itertools

'''
class Solution:
  def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
    xs = sorted([x for x, _ in points])
    print(xs)
    print( max(b - a for a, b in itertools.pairwise(xs)))
obj = Solution()
points = [[8,7],[9,9],[7,4],[9,7]]
obj.maxWidthOfVerticalArea(points)
'''

class Solution:
  def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
    # xs = sorted([x for x, _ in points])4
    xs = sorted([x for x,_ in points]) 
    print(max([b-a for a,b in itertools.pairwise(xs)]))
    
    
obj = Solution()
points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
obj.maxWidthOfVerticalArea(points)