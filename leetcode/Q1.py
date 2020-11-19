# 1
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]
# Time complexity: O(n^2)
# space complexity: O(1)


# 2
def twoSum(nums, target):
    dic = {}
    for index, num in enumerate(nums):
        sub = target - num
        try:
            dic[sub]
            return[dic[sub], index]
        except KeyError:
            dic[num] = index
# Time complexity: O(n)
# space complexity: O(n)
# enumerate: return both index and item


# test
twoSum([2, 7, 11, 15], 9)
# [0, 1]
