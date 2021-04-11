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
    # for functions that changes the value of parameters
    # we'd better deepcopy those parameters
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
# recursion, partition
# O(nlogn) unstable
def quick_sort(nums):
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
# let gap = 1, then it's just Insertion Sort
# O(n^(1 to 2))) depends on gap series
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
# binary heap data structure
# for node i (start form 0), (i-1)//2 is parent node
# 2i+1 is leftchild node, 2i+2 is rightchild
# O(nLogn)
def adjust_heap(nums, i, n):
    # the max of parent and 2 children move to parent
    # then treat parent as the new
    # the stop rules is little complex, attention
    left = 2*i+1
    right = 2*i+2
    max_ = i
    if (left < n) and (nums[left] > nums[max_]):
        max_ = left
    if (right < n) and (nums[right] > nums[max_]):
        max_ = right
    if max_ != i:
        nums[i], nums[max_] = nums[max_], nums[i]
        # after exchange, max_ is not max anymore
        # treat max_ as the new parent and recursion adjust
        adjust_heap(nums, max_, n)


def creat_heap(nums, n):
    # Max-heap: nodes can't have a greater value than its parent
    for i in reversed(range(n//2)):
        adjust_heap(nums, i, n)


def heap_sort(nums):
    nums = deepcopy(nums)
    n = len(nums)
    creat_heap(nums, n)
    for i in reversed(range(n)):
        # exchange the max one (nums[0]) to i
        nums[0], nums[i] = nums[i], nums[0]
        # but the new nums[0] often not the new max
        # so adjust the unexhanged part
        adjust_heap(nums, 0, i)
    return nums


# Merge Sort
# (divide and sort and merge)
# recursion, partition
# O(nLogn)
def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    mid = n//2
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


def merge(left, right):
    result = []
    i_left = 0
    i_right = 0
    while i_left < len(left) and i_right < len(right):
        if left[i_left] <= right[i_right]:
            result.append(left[i_left])
            i_left += 1
        else:
            result.append(right[i_right])
            i_right += 1
    if i_left == len(left)-1:
        result.append(left[i_left])
    if i_right == len(right)-1:
        result.append(right[i_right])
    return result


# with list.pop() the code could be shorter
def merge1(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result.append(left.pop(0))
    if right:
        result.append(right.pop(0))
    return result


# Counting Sort
# the input nums must be non-negative integers with max value k known
# count the same numbers from 0 to k
# O(k+n), it's linear! but if k is huge, not good
def counting_sort(nums):
    # globle variable k should exist
    ints = [0]*(k+1)
    for x in nums:
        ints[x] += 1
    result = []
    for i, count in enumerate(ints):
        while count:
            result.append(i)
            count -= 1
    return result


# Bucket Sort
# divide into different range
# then sort each range
# O(n) to O(n^2), depends on the sort method in each bucket
# here I use shell_sort, and divide into same size ranges
# b: number of buckets
# if counting_sort, just like decrease the space complexity of counting_sort
def bucket_sort(nums):
    # use k//(b-1) to make sure there's b buckets
    # use '//' to filter valuse is not efficient, but
    # not important, there's others methods to divide buckets
    buckets = [[x for x in nums if x//(k//(b-1)) == i] for i in range(b)]
    buckets = [shell_sort(bucket) for bucket in buckets]
    return [x for bucket in buckets for x in bucket]


# Radix sort
# O(kn)
# non-comparing method
# d: biggest number of digital
# LSD (Least significant digital), start from ones digital
def lsd_sort(nums):
    nums = deepcopy(nums)
    for i in range(d):
        buckets = [[] for i in range(10)]
        for x in nums:
            buckets[x//10**i % 10].append(x)
        nums = [x for bucket in buckets for x in bucket]
    return nums


# MSD (Most significant digital), start form maximum digital
def msd_sort(nums):
    def bucket_and_merge(nums, d):
        if d == 0:
            return nums
        d -= 1
        buckets = [[] for i in range(10)]
        for x in nums:
            buckets[x//10**d % 10].append(x)
        for i in range(10):
            buckets[i] = bucket_and_merge(buckets[i], d)
        return [x for bucket in buckets for x in bucket]
    return bucket_and_merge(nums, d)


# test and compare


def runtime(f):
    start = time()
    sort_nums = f(nums)
    end = time()
    for i in range(len(sort_nums)-1):
        if sort_nums[i] > sort_nums[i+1]:
            return numpy.NaN
    return end - start


k = 300
nums = [random.randrange(0, k) for x in range(1000)]
print(runtime(bubble_sort))
print(runtime(selection_sort))
print(runtime(quick_sort))
print(runtime(insertion_sort))
print(runtime(shell_sort))
print(runtime(heap_sort))
print(runtime(merge_sort))
print(runtime(counting_sort))
b = 20
print(runtime(bucket_sort))
d = 3
print(runtime(lsd_sort))
print(runtime(msd_sort))

# bubble_sort 0.0727 s
# selection_s 0.0279 s
# quick_sort 0.0009 s
# insertion_s 0.0339 s
# shell_sort 0.0029 s
# heap_sort 0.0049 s
# merge_sort 0.0029 s
# counting_so 0.0009 s
# bucket_sort 0.0029 s
# lsd_sort 0.0009 s
# msd_sort 0.0019 s
