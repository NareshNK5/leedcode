# class Solution:
#     def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
#         from collections import Counter
#         words2_counter = Counter()
#         for word in words2:
#             word_counter = Counter(word)
#             for letter, count in word_counter.items():
#                 words2_counter[letter] = max(words2_counter[letter], count)
#         res = []
#         for word in words1:
#             word_counter = Counter(word)
#             if all(word_counter[letter] >= words2_counter[letter] for letter in words2_counter):
#                 res.append(word)
#         return res

# speed
# class Solution:
#     def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
#         ans = set(words1)
#         letters = {}
#         for i in words2:
#             for j in i:
#                 count = i.count(j)
#                 if j not in letters or count > letters[j]:
#                     letters[j] = count
                    
#         for i in words1:
#             for j in letters:
#                 if i.count(j) < letters[j]:
#                     ans.remove(i)
#                     break
#         return list(ans)

# memory
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import Counter
        words1_counter = {}
        output_list = []

        words2_counter = Counter()
        for char in words2:
            occurence = Counter(char)
            for counter_data in occurence:
                words2_counter[counter_data] = max(words2_counter[counter_data], occurence[counter_data])
        for i in words1:
            words1_counter = Counter(i)
            if all(words1_counter[word2]>=words2_counter[word2] for word2 in words2_counter):
                output_list.append(i)
        return output_list

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["lo","eo"]
# words2 = ["e","o"]
obj = Solution()
print(obj.wordSubsets(words1,words2))
