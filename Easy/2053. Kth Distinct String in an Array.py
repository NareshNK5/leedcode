# 2053. Kth Distinct String in an Array
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        from collections import Counter
        temp = Counter(arr)
        distinct = [i for i in temp if temp[i] == 1]
        return distinct[k-1] if k <= len(distinct) else ""
            
# class Solution:
#     def kthDistinct(self, arr: List[str], k: int) -> str:
#         store = []
#         for i in range(len(arr)):
#             if arr[i] not in arr[i+1::] and arr[i] not in store:
#                 if k == 1:
#                     return arr[i]
#                 else:
#                     k -= 1
#             store.append(arr[i])
#         return ""
        
arr = ["jqrd","k","miy","svuwg","uv","yttn","bxu","nymzu","dpane","x","mb","zm","ae","ihwtn","kouej","y","zt","h","udx","h","imi","zombs","l","hvt","uor","kzi","tzm","kde","ml","hmvz","hriuy","lav","hlvw","fnnj","bdkh","hu","tuuob","uc","no","qo","ku","foe"]
k = 27
obj = Solution()
res = obj.kthDistinct(arr,k)
print(res)