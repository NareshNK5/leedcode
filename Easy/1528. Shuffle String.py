class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        d={}
        ss=""
        for i,j in zip(indices,s):
            d[i]=j
        x=list(d)
        y=sorted(x)
        for j in y:
            ss+=d[j]
        print(ss)
        return ss
'''
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
    

        n = len(s)
        result = [''] * n  # Create a list to store the shuffled characters

        for i in range(n):
            result[indices[i]] = s[i]  # Place each character in its respective index

        return ''.join(result)
'''
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
obj=Solution()
obj.restoreString(s,indices)
