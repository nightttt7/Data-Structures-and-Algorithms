# slow one, O(n^2)
def len_s(s):
    if s == '':
        return 0
    li = [len(s)]*len(s)
    for i, c in enumerate(s):
        j = 1
        for c1 in s[i+1:]:
            if c1 == c:
                break
            j += 1
        li[i] = j
    for i, x in enumerate(li):
        tmp = x
        for j, x1 in enumerate(li[i+1: i+x]):
            if x1 < x-j-1 and x1+j+1 < tmp:
                tmp = x1+j+1
        li[i] = tmp
    return max(li)


# Sliding Window, O(n)
# if next char is new in f, add it to f
# if next char is shown, cut f from the last shown
def len_s(s):
    d = ""
    f = ""
    for i in range(len(s)):
        if s[i] not in f:
            f += s[i]
        else:
            if len(d) < len(f):
                d = f
            f = f[f.index(s[i])+1::] + s[i]
    return max(len(d), len(f))


len_s('abcabcbb')
# 3
len_s("bbbbb")
# 1
len_s("pwwkew")
# 3
len_s("")
# 0
