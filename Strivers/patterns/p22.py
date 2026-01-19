def pattern22(n):
        for i in range(n):
            for j in range(n):
                print(n-i+j, end="")
            print()

pattern22(4)