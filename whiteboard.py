# Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# Example 1:
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1, 3, 5, 6], target = 7
# Output: 4

# Example 4:
# Input: nums = [1, 3, 5, 6], target = 0
# Output: 0

# Example 5:
# Input: nums = [1], target = 0
# Output: 0

def solution(given_list, target):
    index = 0
    while index < len(given_list):
        if given_list[index] >= target:
            return index
        index += 1
    return index

print(solution([1, 3, 5, 6], 7))
