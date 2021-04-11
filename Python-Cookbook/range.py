list(range(0))
# []

list(range(1))
# [0]
# 1 number start form 0

list(range(5))
# [0, 1, 2, 3, 4]
# 5 number start form 0
# start from 0, end to (5-1)

list(range(0, 5))
# same as list(range(5))

list(range(3, 5))
# [3, 4]
# start from 3, end to (5-1)
# consider [3, 5), include 3, not include 5

for x in range(3, 10):
    print(x)
# range() used for iterating

list(range(3, 10, 2))
# [3, 5, 7, 9]

[x/2 for x in range(3, 10)]
# [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

list(range(3, 10))[::-1]
# [9, 8, 7, 6, 5, 4, 3]
