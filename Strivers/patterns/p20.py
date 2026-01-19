def pattern19(n):
        mid = n // 2
        for i in range(mid+1):
            l = i
            r = n-i
            for j in range(n):
                if j < l or j >= r:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        for i in range(mid-1, -1,-1):
            l = i
            r = n-i
            for j in range(n):
                if j < l or j >= r:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        
pattern19(10)