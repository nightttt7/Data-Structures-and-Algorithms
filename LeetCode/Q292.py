# Nim Game DP, O(n)
def canWinNim(n):
    cache = [1]*n
    # (cache[0:3] or n = 1,2,3) = 1
    # loop start from n = 4, cache[3]
    for i in range(4, n+1):
        if cache[(i-1)-3] * cache[(i-1)-2] * cache[(i-1)-1] == 1:
            cache[i-1] = 0
    # return n = n, cache[n-1]
    return cache[n-1]


# analysis result:
# n = 1,2,3 win
# n = 4 loss
# n = 5,6,7 win
# 1. you can find the regular pattern, n % 4 == 0 loss, others win, no ask why
# 2. in fact we can get the best strategy:
#   you: take k and let (n-k) % 4 != 0, friend take t,you always take (4-t)
#        at last you will win when n in [5,6,7]
#   friend: if n % 4 == 0, you take k, friend will always take (4-k)
#           at last you will always meet n = 4, loss
def canWinNim(n):
    return n % 4 != 0


# oh, this is faster
def canWinNim(n):
    return n % 4


# WTF, Python
def canWinNim(n):
    b = bin(n)
    return b[-1] == '1' or b[-2] == '1'
