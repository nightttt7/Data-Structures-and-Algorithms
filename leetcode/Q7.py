def int_reverse(x):
    if x < 0:
        num_str = str(x)[:0:-1]
        symbol = -1
    else:
        num_str = str(x)[::-1]
        symbol = 1
    output = symbol*int(num_str)
    if abs(output) > 2147483647:
        return 0
    else:
        return output
# sometimes string operation is faster
