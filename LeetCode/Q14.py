# Brute Force
strs = ["flower", "flow", "flight"]


# Horizontal scanning
# compare each with number one
def prefix(strs):
    if len(strs) == 0:
        return ''
    prefix = strs[0]
    for x in strs[1:]:
        while len(prefix) > len(x):
            prefix = prefix[:-1]
        while prefix != x[:len(prefix)]:
            prefix = prefix[:-1]
            if len(prefix) == 0:
                return ''
    return prefix
# time complexity: O(S). S is len(strs)
# space complexity: O(1)


# Vertical scanning
# check first 1, 2, 3 ... char
def prefix(strs):
    n = min([len(x) for x in strs])
    if n == 0:
        return ''
    else:
        prefix = ''
        for i in range(n):
            if len(set([x[i] for x in strs])) == 1:
                prefix = strs[0][:i+1]
            else:
                return prefix
    return prefix
# time complexity: O(S). S is len(strs)
# space complexity: O(1)
