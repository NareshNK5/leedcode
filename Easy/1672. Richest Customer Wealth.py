class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        r=0
        for i in range(len(accounts)):
            s=0
            for j in range(len(accounts[i])):
                s+=accounts[i][j]
            if r<s:
                r=s
        return r
                
                
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richier = 0
        for customer in accounts:
            customer_wealth = sum(customer)
            richier = max(customer_wealth, richier)
        return richier
'''
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = lambda x: sum(x)
        return max([i for i in map(res, accounts)])

'''

obj = Solution()
accounts = [[1,5],[7,3],[3,5]]
obj.maximumWealth(accounts)        