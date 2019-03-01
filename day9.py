def totalFlips(A, B, C, N): 
  
    count = 0
    for i in range(N): 
          
        if A[i] == B[i] and C[i] == '1': 
            count=count+1
  
        elif A[i] != B[i] and C[i] == '0': 
            count=count+1
    return count 
N = 5
a = "10100"
b = "00010"
c = "10011"
print(totalFlips(a, b, c, N)) 
