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


# 3
# similiar with Q167, two sum (input array is sorted)
# for better understanding: https://www.cxyxiaowu.com/9769.html
def twoSum(nums, target):
    nums_index = [(v, index) for index, v in enumerate(nums)]
    nums_index.sort()
    begin = 0
    end = len(nums) - 1
    while True:
        curr = nums_index[begin][0] + nums_index[end][0]
        if curr == target:
            return [nums_index[begin][1], nums_index[end][1]]
        elif curr < target:
            begin += 1
        else:
            end -= 1


# test
twoSum([2, 7, 11, 15], 9)
# [0, 1]
