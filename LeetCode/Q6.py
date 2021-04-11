def convert(s, numRows):
    if numRows == 1:
        return s

    def add1(x):
        return x+1

    def sub1(x):
        return x-1

    dic = {i: [] for i in range(numRows)}
    j = 0
    f = add1
    for i, c in enumerate(s):
        dic[j].append(c)
        j = f(j)
        if j == 0:
            f = add1
        if j == numRows-1:
            f = sub1
    return ''.join([w for value in dic.values() for w in value])
# O(n)


s = 'aekfbglhcimjd'
numRows = 3
convert(s, numRows)
# 'abcdefghijklm'
