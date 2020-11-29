# references:
#   https://runestone.academy/runestone/books/published/pythonds/index.html
from copy import deepcopy


# sum numbers with recursion
def sum_recursion(nums):
    if nums:
        if len(nums) == 1:
            return nums[0]
        else:
            return nums[0] + sum_recursion(nums[1:])
    else:
        return 0


# The Three Laws of Recursion
# must have a base case
# must change its state and move toward the base case
# must call itself, recursively


# convert decimal to binary, hexadecimal or other base (<=16) number
def convert(decimal, base):
    extend_num_string = "0123456789ABCDEF"
    if decimal < base:
        return extend_num_string[decimal]
    return convert(decimal//base, base) + extend_num_string[decimal % base]


# use stack to implement recursion
def convert_stack(decimal, base):
    decimal = deepcopy(decimal)
    extend_num_string = "0123456789ABCDEF"
    stack = []
    output = ''
    while decimal > 0:
        stack.append(extend_num_string[decimal % base])
        decimal = decimal // 2
    while stack:
        output += stack.pop()
    return output


# Tower of Hanoi
# a helpful pic for this algorithm:
# https://en.wikipedia.org/wiki/Tower_of_Hanoi#/media/File:Tower_of_Hanoi_recursion_SMIL.svg
# the most important thing:
#   no need to follow or clear the whole process
#   only need to know what the function do
#   and make sure a problem could be solves by solving smaller problem
#   and how to solve the minimum problem
def move(i, start, end, mid):
    if i >= 1:
        move(i-1, start, mid, end)
        print('move {} from {} to {}'.format(i, start, end))
        move(i-1, mid, end, start)


move(5, 'A', 'C', 'B')


# making change using the fewest coins
# 1. inefficient way, compare with any possible cases, just like brute force
def make_change1(coin_list, change):
    min_coins = change
    if change in coin_list:
        return 1
    else:
        for i in coin_list:
            if i < change:
                num_coins = make_change1(coin_list, change-i) + 1
                if num_coins < min_coins:
                    min_coins = num_coins
    return min_coins


# 2. with caching technique, remember the known information
def make_change2(coin_list, change, known_dict={}):
    min_coins = change
    if change in known_dict:
        return known_dict[change]
    elif change in coin_list:
        known_dict[change] = 1
        return 1
    else:
        for i in coin_list:
            if i < change:
                num_coins = make_change2(coin_list, change-i, known_dict) + 1
                if num_coins < min_coins:
                    min_coins = num_coins
        known_dict[change] = min_coins
    return min_coins


# 3. Dynamic programming
# extend min_coins_dict for each iteration
# could get a dict for result of change in range(1, input+1)
def make_change3(coin_list, change):
    min_coins_dict = {}
    # start from 0, because we need min_coins_dict[0] = 0
    for x in range(change+1):
        num_coins = x
        for i in coin_list:
            # NB! here use i <= x, not i<x as before
            if i <= x and min_coins_dict[x-i]+1 < num_coins:
                num_coins = min_coins_dict[x-i]+1
        min_coins_dict[x] = num_coins
    return min_coins_dict


make_change1([1, 5, 10, 20], 63)
make_change2([1, 5, 10, 20], 63)
make_change3([1, 5, 10, 20], 63)
