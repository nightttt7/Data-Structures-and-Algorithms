# references:
#   https://brilliant.org/wiki/sorting-algorithms/
#   https://blog.csdn.net/xutiantian1412/article/details/100057566

# initial
import random
import numpy
from time import time
from copy import deepcopy


# Bubble Sort
# O(N^2)
def bubble_sort(nums):
    nums = deepcopy(nums)
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


# Selection Sort
# exchange the min value directly
# less move than Bubble Sort
# O(n^2)
def selection_sort(nums):
    nums = deepcopy(nums)
    for i in range(len(nums)-1):
        min_i = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_i]:
                min_i = j
        nums[i], nums[min_i] = nums[min_i], nums[i]
    return nums


# Quick Sort
# average-case: O(nlogn)
def quick_sort(nums):
    nums = deepcopy(nums)
    if len(nums) <= 1:
        return nums
    left = []
    right = []
    pivot_list = []
    pivot = nums[0]
    for x in nums:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            pivot_list.append(x)
    left = quick_sort(left)
    right = quick_sort(right)
    return left+pivot_list+right


# Insertion Sort
# O(n^2)
def insertion_sort(nums):
    nums = deepcopy(nums)
    for i in range(1, len(nums)):
        curr = nums[i]
        test_i = i-1
        while (test_i >= 0) and (curr < nums[test_i]):
            nums[test_i+1] = nums[test_i]
            test_i -= 1
        nums[test_i+1] = curr
    return nums


# Shell Sort
# O(n^1.3)
# let gap = 1, then it's just Insertion Sort
def shell_sort(nums):
    nums = deepcopy(nums)
    gap = len(nums)//2
    while gap > 0:
        for i in range(gap, len(nums)):
            curr = nums[i]
            test_i = i-gap
            while (test_i >= 0) and (curr < nums[test_i]):
                nums[test_i+gap] = nums[test_i]
                test_i -= gap
            nums[test_i+gap] = curr
        gap = gap//2
    return nums


# Heap Sort
# TBC


# test


def runtime(f):
    start = time()
    sort_nums = f(nums)
    end = time()
    for i in range(len(sort_nums)-1):
        if sort_nums[i] > sort_nums[i+1]:
            return numpy.NaN
    return end - start


nums = [random.randrange(0, 1000) for x in range(1000)]
print(runtime(bubble_sort))
print(runtime(selection_sort))
print(runtime(quick_sort))
print(runtime(insertion_sort))
print(runtime(shell_sort))