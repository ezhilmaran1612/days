def countXOR(n): 
      
    count0, count1 = 0, 0
    while (n != 0): 
      
        # calculating count of zeros and ones 
        if(n % 2 == 0):  
            count0 += 1
        else: 
            count1 += 1
        n //= 2
          
    return (count0 ^ count1) 
      
# Driver Code 
n = 31
print(countXOR(n)) 