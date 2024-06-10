class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        al=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        al1=["a","b","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        word=[]
        s=""
        for i in words:
            for k in range(len(str(i))):
                for j in range(len(al)):
                    if i[k]==al1[j]:
                        s+=al[j]
            word.append(s)
            s=""
        print(len(set(word)))
    '''
    class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        LETTERS = list(string.ascii_lowercase)
        CODES = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
        "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        LETTER_TO_CODE = { k:v for (k,v) in zip(LETTERS, CODES) }

        transforms = set()
        # translate each word into Morse code and add to set (transforms)
        for word in words:
            code = ""
            for letter in word:
                code += LETTER_TO_CODE[letter]
            transforms.add(code)

        # return length of transforms
        return len(transforms)
    '''
words = ["a"]
obj = Solution()
obj.uniqueMorseRepresentations(words)