import math 
  
def swapBitsInPair( x): 
  
    return ((x & 0b10101010) >> 1) or ((x & 0b01010101) << 1) 
   
x = 4;  
print(swapBitsInPair(x))