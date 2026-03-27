class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        temp,kelvin,farheit  = [],round(celsius + 273.15,2),round(celsius * 1.80 + 32.00,3)
        temp.append(round(kelvin,5))
        temp.append(round(farheit,5))
        return temp
