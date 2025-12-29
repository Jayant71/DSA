# Linear Search

# Testing ARRAY
# import array

# nums = array.array("i", [23, 65, 2, 5, 76, 14, 10])

# print(nums.index(76))


def linear_search(numbers: list[int], k: int):
    for i in range(len(numbers)):
        if (numbers[i] == k):
            return i
    return -1


nums = [23, 65, 2, 5, 76, 14, 10]

k = 2
print(linear_search(nums, k))
