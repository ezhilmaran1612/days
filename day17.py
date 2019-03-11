def toggleBitsFromLToR(n, l, r): 
      
    num = (((1 << r) - 1) ^  
           ((1 << (l - 1)) - 1)) 
    return (n ^ num) 
      
def unsetBitsInGivenRange(n, l, r): 
    num = (1 << (4 * 8 - 1)) - 1
  
    num = toggleBitsFromLToR(num, l, r) 
  
    return (n & num) 

n = 42
l = 2
r = 5
print(unsetBitsInGivenRange(n, l, r))