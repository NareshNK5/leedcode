class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        for i in range(len(accounts)):
            accounts[i]=sum(accounts[i])
        print(max(accounts))
        return max(accounts)
obj=Solution()
accounts = [[2,8,7],[7,1,3],[1,9,5]]
obj.maximumWealth(accounts)
