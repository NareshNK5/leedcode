class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiou'
        consonant = 'qwrtypsdfghjklzxcvbnm'
        vowels += vowels.upper()
        consonant += consonant.upper()
        allowed = vowels + consonant + '0987654321'
        if len(word)<3:return False
        has_vowels = False
        has_consonant = False
        for c in word:
            if c in vowels: has_vowels =  True
            if c in consonant: has_consonant =  True
            if c not in allowed: return False
        return has_consonant and has_vowels
obj = Solution()
word = "b3"
obj.isValid(word)