def pattern(num):
    k = num
    for i in range(k, 0, -1):
        for j in range(k, 0,-1):
            print(end=" ")
        k = k+1
        for j in range(0,i):
            print("*",end=" ")
        print (" ")
    n = k-1
    for i in range(0,num):
        for j in range(n,0,-1):
            print(end=" ")
        n = n-1
        for j in range(0,i+1):
            print("*",end=" ")
        num=num+1
        print(" ")

pattern(10)
