from typing import List
# def searchRange(nums, target):
#     pos = [-1, -1]
#     for idx in range(len(nums)):
#         if (pos[1] == -1 and nums[idx] == target):
#             pos[0] = pos[1] = idx
#             continue
#         if (nums[idx] == target):
#             pos[1] = idx
#     return pos

def searchRange(nums: List[int], target: int) -> List[int]:
        pos = [-1,-1]
        size = len(nums)
        for i in range(size):
            if pos[0] == -1 and nums[i] == target:
                pos[0] = pos[1] = i
                for j in range(i, size):
                    if nums[j] == target:
                        print(j )
                        if j == size -1:
                            print(j)
                            pos[1] = j
                            return pos
                        continue
                    pos[1] = j-1
                    return pos
        return pos

# nums = [5, 7, 7, 8, 10, 10]
nums = [5 for _ in range(1000)]
target = 5

print(searchRange(nums, target))
