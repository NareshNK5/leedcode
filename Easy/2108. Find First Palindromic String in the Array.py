# 2108. Find First Palindromic String in the Array
class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        return next((word for word in words if word == word[::-1]), "")

        # for i in range(len(words)):
        #     if words[i] == words[i][::-1]:
        #         return words[i]
        # return ""
        
words = ["abc","car","ada","racecar","cool"]
obj = Solution()
res = obj.firstPalindrome(words)
print(res)