# Binary Search

# Condition: The array/list must be sorted

# Using recursion

def binary_search(numbers: list[int], k: int, start: int, end: int):
    mid: int = (start + end) // 2
    if start > end:
        return -1
    if numbers[mid] == k:
        return mid
    elif (numbers[mid] > k):
        return binary_search(numbers, k, start, mid-1)
    elif (numbers[mid] < k):
        return binary_search(numbers, k, mid + 1, end)

# Using loops


def binary_search_loop(numbers: list[int], k: int):
    size = len(numbers)
    start, end = 0, size-1

    while (start <= end):
        mid: int = (start + end) // 2
        if (numbers[mid] == k):
            return mid
        elif (numbers[mid] > k):
            end = mid - 1
        elif (numbers[mid] < k):
            start = mid + 1
    return -1


nums = [2, 5, 14, 21, 23, 65, 76]

k = 14
print(binary_search(nums, k, 0, len(nums)-1))
print(binary_search_loop(nums, k))
