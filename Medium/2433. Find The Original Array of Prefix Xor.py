class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        print(pref)
        nl=[pref[0]]
        for i in range(len(pref)-1):
            c=pref[i+1]^pref[i]
            nl.append(c)
        print(nl)
pref = [13]
obj = Solution()
obj.findArray(pref)


'''
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = []
        next_num = 0
        for num in pref:
            arr.append(num ^ next_num)
            next_num = num
        return arr  
'''