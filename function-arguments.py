# accept any number of arguments (positional and keywork arguments together)
def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)


# only accept specific keyword arguments
def onlykwargs(arg, *, kwarg):
    print(kwarg)


def onlykwargs(*args, kwarg):
    print(kwarg)


# multiple returns
def myfun():
    return 1, 2, 3


a = (1, 2)
b = 1, 2
a == b
# output: True


# function with default arguments
# if default value is list, set or dict
def myfun(a, b=None):
    if b is None:
        b = []


# if is to check any b value supplied (include None, 0 or False)
_no_value = object()


def myfun(a, b=_no_value):
    if b is _no_value:
        print('no b value supplied')
