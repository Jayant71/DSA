def searchRange(nums, target):
    pos = [-1, -1]
    for idx in range(len(nums)):
        if (pos[1] == -1 and nums[idx] == target):
            pos[0] = pos[1] = idx
            continue
        if (nums[idx] == target):
            pos[1] = idx
    return pos


nums = [5, 7, 7, 8, 8, 10]
target = 8

print(searchRange(nums, target))
