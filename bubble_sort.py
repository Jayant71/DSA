# Bubble Sort

import random


def bubble_sort(arr: list[int]):
    for j in range(len(arr)-1):
        # bubbling the last (largest) element so length unsorted reduces by 1 after each iteration
        for i in range(len(arr)-1-j):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


# nums = [23, 65, 2, 5, 76, 14, 10]
nums = [random.randint(1, 10000) for _ in range(100)]

k = 2
print(nums)

# pass a copy (does not sorts the original array)
print(bubble_sort(nums.copy()))
print(nums)  # still unsorted

# pass by reference (sorts the original array)
print(bubble_sort(nums))
print(nums)  # still sorted
