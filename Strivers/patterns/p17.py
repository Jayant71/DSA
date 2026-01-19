def pattern7(n):
        mid = (2*n) //2
        for i in range(n):
            l = mid - i
            r = mid + i
            c = 0
            for j in range(2*n):
                if l <= j <= mid:
                    print(chr(65+c), end="")
                    c += 1
                elif mid < j <= r:
                    c -= 1
                    print(chr(65+c-1), end="")
                else:
                     print(" ", end="")
            print()
pattern7(4)