class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for word in words:
            word_set = set(word.lower())
            if any(word_set.issubset(keyboard_row) for keyboard_row in keyboard_rows):
                res.append(word)
        return res
    
# words = ["Hello","Alaska","Dad","Peace"]
words = ["omk"]
# words = ["adsdf","sfd"]
obj = Solution()
print(obj.findWords(words))