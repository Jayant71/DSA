import random


def countNegatives(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])-1, -1, -1):
            if (grid[i][j] < 0):
                count += 1

    return count


grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
# grid = []
m = 3
n = 4

# grid = [[random.randint(-10, 10) for _ in range(n)] for _ in range(m)]
# for row in grid:
#     row.sort(reverse=True)

print(grid)
print(countNegatives(grid))
