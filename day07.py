def findPattern(n): 
  
    prev = n % 2
    n = n // 2

    while (n > 0): 
      
        curr = n % 2

        if (curr == prev): 
            return False
  
        prev = curr 
        n = n // 2
      
    return True

n = 10
print("Yes") if(findPattern(n)) else print("No")