class Solution:
    def sortSentence(self, s: str) -> str:
        print(s)
        ns = s.split(" ")
        print(ns)
        print(s)
        for i in ns:
            print(i,i[-1])
            for j in range(0,len(i)+1):
                if j == i[-1]:
                    print(i[:-1])
                    ns.insert(int(i[-1]),i[:-1])
        print(ns)
s = "is2 sentence4 This1 a3"
# s = "is2"
obj = Solution()
obj.sortSentence(s)