def pattern18(n):
        for i in range(n):
            for j in range(n):
                if j <= i:
                    print(chr(65+n-i+j-1), end=" ")
                else:
                    print(" ", end="")
            print()

pattern18(5)