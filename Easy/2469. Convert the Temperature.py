# 2469. Convert the Temperature

class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius+273.15,celsius*1.80+32]
        
obj = Solution
celsius=36.50
obj.convertTemperature(celsius)