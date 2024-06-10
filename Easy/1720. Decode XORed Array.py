class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        arr=[first]
        for i in encoded:
            arr.append(arr[-1] ^ i)
        return arr
            
encoded = [1,2,3]
first = 1
obj=Solution()
obj.decode(encoded,first)
