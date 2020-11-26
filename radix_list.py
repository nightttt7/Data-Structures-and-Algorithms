# radix_list: return a list of radixes for each digital of a int number
# d: the maximum digital
# x: int number


def radix_list_1(x, d):
    x_str = str(x)
    n = len(x_str)
    x_str = '0'*(d-n)+x_str
    return [int(x_str[i]) for i in range(d)]


def radix_list_2(x, d):
    return [x//10**i % 10 for i in reversed(range(d))]


# digital3: fastest for most cases
def radix_list_3(x, d):
    x_str = str(x)
    output = [0]*d
    for i, c in enumerate(reversed(x_str)):
        output[-i-1] = int(c)
    return output


# test
x = 59818465165
d = 15
print(radix_list_1(x, d))
print(radix_list_2(x, d))
print(radix_list_3(x, d))
