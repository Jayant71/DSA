def pattern7(n):
        mid = (2*n) //2
        for i in range(n):
            l = mid - i
            r = mid + i
            for j in range(2*n):
                if l <= j <= r:
                    print("*", end="")
                else:
                     print(" ", end="")
            print()
pattern7(5)