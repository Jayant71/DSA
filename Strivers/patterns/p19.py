def pattern19(n):
        mid = n // 2
        for i in range(mid):
            l = mid - i
            r = mid + i
            for j in range(n):
                if l <= j < r:
                    print(" ", end="")
                else:
                    print("*", end="")
            print()
        for i in range(mid-1,-1,-1):
            l = mid - i
            r = mid + i
            for j in range(n, 0,-1):
                if l < j <= r:
                    print(" ", end="")
                else:
                    print("*", end="")
            print()

pattern19(10)