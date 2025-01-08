class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        count = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count+=1
        return count


# words = ["pa","papa","ma","mama"]
# words = ["a","aba","ababa","aa"]
words = ["a","abb"]
obj = Solution()
print(obj.countPrefixSuffixPairs(words))