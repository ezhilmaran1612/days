def toggleBitsFromLToR(n, l, r): 
  
    if (r < l): 
        return n 
   
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1) 
   
    return (n ^ num) 
  
def smallNumWithNSetAndMUnsetBits(n, m): 
  
    num = (1 << (n + m)) - 1
   
    return toggleBitsFromLToR(num, n, n + m - 1); 
n = 2
m = 2
  
ans = smallNumWithNSetAndMUnsetBits(n, m) 
print (ans)