# 2000. Reverse Prefix of Word

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            s = word.split(ch,1)
            print(s[0][::-1])
            print(ch+s[0][::-1]+s[1])
        else:
            print(word)
            
'''
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        n=word.index(ch)
        return word[:n+1][::-1]+word[n+1:]
'''
        
obj = Solution()
word = "abcdefd"
ch = "d"
obj.reversePrefix(word,ch)