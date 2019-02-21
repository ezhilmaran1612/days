import math 
def getRightMostSetBit(n): 
  
    return math.log2(n & -n) + 1
def posOfRightMostDiffBit(m, n): 
  
    return getRightMostSetBit(m ^ n) 
  
m = 52
n = 4
print("position = ", int(posOfRightMostDiffBit(m, n))) 