def pattern6(n):
        for i in range(n,0,-1):
            for j in range(i):
                print(j+1, end="")
            print()
pattern6(5)