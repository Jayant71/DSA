def pattern15(n):
        for i in range(n):
            for j in range(n,i,-1):
                print(chr(65+(n-j)), end="")
            print()

pattern15(5)