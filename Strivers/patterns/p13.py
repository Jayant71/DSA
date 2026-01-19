def pattern13(n):
        counter = 1
        for i in range(n):
            for j in range(i+1):
                print(counter, end = " ")
                counter += 1
            print()

pattern13(5)