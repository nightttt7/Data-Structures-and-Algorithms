# references: https://runestone.academy/runestone/books/published/pythonds/SortSearch/searching.html


# 1. Sequential Search: from start to end one by one
# 2. Binary Search
# alist is sorted from small to big
def binary_search(alist, item):
    left = 0
    right = len(alist)-1
    while left <= right:
        mid = (left+right)//2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            left = mid+1
        else:
            right = mid-1
    return False


# alist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# item = 100
# binary_search(alist, item)


# 3. Hashing
# write a good hash function, such as
def hash_func(item, size):
    return item % size
# get a position, put items into a list with this pos


# handle collisions:
# a. open addressing
# (1). find the next open position
# (2). rehash until no collisions
# to make sure all pos be tested, size is better to be a prime
# the value add could be quadratic raising
def rehash(pos, size):
    return (pos+3) % size


# b. separate chaining
# many items exist at the same location in the hash table

# for a item, hash it and get position, return True or False
# Dictionary data structure could be implemented by hashing
