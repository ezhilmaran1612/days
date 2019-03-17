def findSum(n) : 
  
    sum = 0
    i = 1
    while((1 << i) < n ) : 
        for j in range(0, i) :  
            num = (1 << i) + (1 << j)  
  
            if (num <= n) : 
                sum += num 
          
        i += 1
          
    return sum
  
n = 10
print(findSum(n))