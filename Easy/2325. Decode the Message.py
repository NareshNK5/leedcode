import string
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        p = ""
        for char in key:
            if char not in p and p!=None:
                p = p+char
        p=p.replace(" ","")
        # print(p)
        al = list(zip(p,string.ascii_lowercase))
        print(al)
        # print(al[0][1],len(p))
        for i in range(len(key)):
            for j in range(len(key)-1):
                # print(al[j][0],message[j])
                if al[j][0]==message[i]:
                    print(al[j][1])
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
obj = Solution()
obj.decodeMessage(key,message)