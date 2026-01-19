def pattern10(n):
        for i in range(n):
            print("*"*(i+1))
        for i in range(n-1,0,-1):
            print("*"*(i))

pattern10(5)