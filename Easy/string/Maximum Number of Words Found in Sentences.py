class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        print(sentences)
        splt=[]
        x=0
        for i in range(len(sentences)):
            count=1
            for j in sentences[i]:
                if j==" ":
                    count+=1
                else:
                    count+=0
            splt.append(count)
        print(splt)
        ma=0
        for i in splt:
            if i > ma:
                ma=i
        #print(ma)
        return ma
        '''
        splt=[12,78,15,8]
        for k in range(len(splt)-1):
            for l in range(len(splt)-1):
                if splt[k]>splt[k+1]:
                    splt[k],splt[k+1]=splt[k+1],splt[k]
                    print(splt)
           

        a=10
        b=20
        a,b=b,a
        print(a,b)
        c=a
        a=b
        b=c
        print(a,b)
    '''            
            
obj=Solution()
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
obj.mostWordsFound(sentences)

