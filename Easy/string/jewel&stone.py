class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        total=[]
        # print(jewels, stones)
        for i in jewels:
            for j in stones:
                # print(i,j)
                if i == j:
                    total.append(i)
                    tot=len(total)
                else:
                    tot=len(total)+0
        # print(tot)
        return tot
                
            
obj=Solution()
'''
jewels = "aA"
stones = "aAAbbbb"

'''
jewels = "z"
stones = "ZZ"

print(obj.numJewelsInStones(jewels, stones))

