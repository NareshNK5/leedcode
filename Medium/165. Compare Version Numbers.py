# 165. Compare Version Numbers
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=int(version1.split("."))
        version2=int(version2.split("."))
        for i in version1:
            for j in version2:
                
        
obj = Solution()
version1 = "0.1"
version2 = "1.1"
obj.compareVersion(version1,version2)