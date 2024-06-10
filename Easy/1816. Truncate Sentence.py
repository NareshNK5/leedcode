class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        s = s[:4]
        s = ' '.join(s)
        return s
s = "Hello how are you Contestant"
k = 4
obj = Solution()
obj.truncateSentence(s,k)