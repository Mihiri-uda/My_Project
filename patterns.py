def pattern(n):
    k=2* n-2
    for i in range(1,n):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k-1
        for j in range(0, i+1):
            print ("0", end= " ")
        print("\r")
pattern(5)
