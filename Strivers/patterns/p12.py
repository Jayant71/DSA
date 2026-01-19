def pattern12(n):
        for i in range(1,n+1):
            for j in range(1, 2*n+1):
                if j <= i or j >= 2*n-i+1:
                        if j > n:
                            print(2*n-j+1, end = "")
                        else:
                            print(j, end = "")
                else:
                      print(" ", end="")
                  
            print()

pattern12(4)