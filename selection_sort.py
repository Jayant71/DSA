# Selection Sort
import random


# Find index of minimum element
def minimum_idx(arr, start):
    _minimum = start
    for i in range(start, len(arr)):
        if (arr[_minimum] > arr[i]):
            _minimum = i
    return _minimum


def selection_sort(arr: list):
    for i in range(len(arr)):
        min_idx = minimum_idx(arr, i)
        # min_idx = arr.index(min(arr[i:])) # Single line alternative for finding index of minimum element (no need to define the minimum_idx function separately)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


nums = [23, 65, 2, 5, 76, 14, 10]
# nums = [random.randint(1, 10000) for _ in range(100)]

print(nums)

# pass a copy (does not sorts the original array)
# print(selection_sort(nums.copy()))
# print(nums)  # still unsorted

# pass by reference (sorts the original array)
print(selection_sort(nums))
print(nums)  # still sorted
