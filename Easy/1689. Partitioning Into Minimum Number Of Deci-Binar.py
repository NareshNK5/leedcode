# 1689. Partitioning Into Minimum Number Of Deci-Binar

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(i) for i in n)