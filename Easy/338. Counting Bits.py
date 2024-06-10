# class Solution:
#     def countBits(self, n: int) -> list[int]:
#         res=[]
#         res1=[]
#         x=[bin(i)[2:].count("1") for i in range(n+1)]
#         print(x)
        
#         # for j in range(len(x)):
#         #     for k in x[j]:
#         #         res1.append(int(k))
#         #     res.append(sum(res1))
#         #     res1=[]
#         # print(res)
            


class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0] * (n+1)
        print(res)
        for i in range(n+1):
            print(res[i>>1] , (i&1))
            res[i] = res[i>>1] + (i&1)
        print(res)



obj = Solution()
n = 5
obj.countBits(n)
