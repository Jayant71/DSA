# Insertion Sort

import random


def insertion_sort(arr):
    for i in range(len(arr)-1):
        if (arr[i+1] > arr[i]):
            continue

        for j in range(i, -1, -1):
            if (arr[j] > arr[j+1]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
            else:
                break
    return arr


# nums = [23, 65, 2, 5, 76, 14, 10]
nums = [random.randint(1, 100) for _ in range(25)]

print(nums)

# pass a copy (does not sorts the original array)
# print(insertion_sort(nums.copy()))
# print(nums)  # still unsorted

# pass by reference (sorts the original array)
print(insertion_sort(nums))
print(nums)  # still sorted
