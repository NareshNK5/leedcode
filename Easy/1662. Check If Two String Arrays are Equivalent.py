class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        word1 = ''.join(word1)
        word2 = ''.join(word2)
        if word1 == word2:
            print(True)
        else:
            print(False)
'''
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        str2 = ""
        for s in word1:
            str1 += s
        for s in word2:
            str2 += s
        return str1 == str2
'''
word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]
obj = Solution()
obj.arrayStringsAreEqual(word1,word2)