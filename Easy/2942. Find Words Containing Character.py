# 2942. Find Words Containing Character

class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        res=[]
        for i in range(len(words)):
            print(i)
            if x in words[i]:
                res.append(i)
        print(res)
                

words = ["leet","code"]
x = "e"
obj = Solution()
obj.findWordsContaining(words,x)

'''
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indexes = []
        for index, word in enumerate(words):
            if x in word:
                indexes.append(index)
        return indexes

'''