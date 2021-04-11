# Anonymous function
afun = lambda x: x * x
afun(5)

# bind arguments when generate lambda function
funs = [lambda x, n=n: x+n for n in range(5)]
for f in funs:
    print(f(0))
# output: 0, 1, 2, 3, 4

# or arguments will not be dynamic
funs = [lambda x: x+n for n in range(5)]
for f in funs:
    print(f(0))
# output: 4, 4, 4, 4, 4
