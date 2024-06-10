# # class Solution:
# #     def sumOddLengthSubarrays(self, arr: list[int]) -> int:
#         # sum1=0
#         # i=len(arr)
#         # if i <= 2:
#         #     for j in arr:
#         #         sum1+=j
#         #     print(sum1)
#         # elif i <= 4:
#         #     for j in arr:
#         #         sum1+=j
#         #     print(sum1*2)
#         # elif i <= 6:
#         #     for j in range(len(arr)):
#         #         if j<=2:
#         #             sum2=sum(arr[j:(j+3)])
#         #             sum1+=sum2
#         #     print(sum1+(sum(arr)*2))
                

#         # sum1=0
#         # sum2=0
#         # for i in arr:
#         #     sum1+=i
#         # print("sum1",sum1)
#         # for j in range(len(arr)):
#         #     if j<=2:
#         #         sum2=sum(arr[j:(j+3)])
#         #         l=len(sum2)
#         #         print(l)
#         #         if l==3:
#         #             print(sum2)
#         #             sum1+=sum2
#         # print("sum1",sum1)

#         # a1=[]
#         # c=0
#         # s=0
#         # d=0
#         # for i in arr:
#         #     s+=i
#         # for i in range(len(arr)-1):
#         #     for j in range(i,len(arr)):
#         #         a1.append(arr[j])
#         #         if len(a1)==3:
#         #             c+=sum(a1)
#         #             a1.clear()
#         #             break
#         # for i in range(len(arr)-1):
#         #     for j in range(i,len(arr)):
#         #         a1.append(arr[j])
#         #         if len(a1)==5:
#         #             d+=sum(a1)
#         #             a1.clear()
#         #             break
#         # print(d+c+s)

# # class Solution:
# #     def sumOddLengthSubarrays(self, arr: list[int]) -> int:
# #         n = len(arr)
# #         answer = 0
# #         for i in range(n):
# #             for j in range(i,n):
# #                 if (j - i + 1) % 2 == 1:
# #                     print(i,j)
# #                     current_sum = 0
# #                     for index in range(i, j + 1):
# #                         print("index",index)
# #                         current_sum += arr[index]
# #                     answer += current_sum
# #         print(answer)
# #         return answer

# class Solution:
#     def sumOddLengthSubarrays(self, arr: list[int]) -> int:
#         n = len(arr)
#         answer = 0
#         for i in range(n):
#             current_sum = 0
#             for j in range(i, n):
#                 current_sum += arr[j]
#                 answer += current_sum if (j - i + 1) % 2 == 1 else 0
#         return answer

# arr = [10,11,12]
# obj=Solution()
# obj.sumOddLengthSubarrays(arr)

class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        l=len(arr)
        s=0
        for i in range(l):
            for j in range(i,l):
                if (j-i+1)%2==1:
                    for k in range(i,j+1):
                        s+=arr[k]
        print(s)
arr = [10,11,12]
obj=Solution()
obj.sumOddLengthSubarrays(arr)