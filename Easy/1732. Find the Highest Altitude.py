class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        l=[0]
        for i in range(len(gain)):
            c=l[i]+gain[i]
            l.append(c)
        return max(l)
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for g in range(len(gain)):
            altitudes.append(altitudes[g] + gain[g])
        return(max(altitudes))
'''
gain = [-4,-3,-2,-1,4,3,2]
obj = Solution()
obj.largestAltitude(gain)