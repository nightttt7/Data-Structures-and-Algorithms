# O(n^2), code is little long, algo is good
def longestPalindrome(s: str):
    longest = s[0]
    n = len(s)
    if n == 1:
        return longest
    len_max = 0
    i = 0
    while True:
        if i+2 < n:
            if (s[i] == s[i+2]):
                j = 0
                len_ = 3
                pal = s[i: i+3]
                while (i-j >= 0) and (i+2+j < n):
                    if s[i-j] == s[i+2+j]:
                        len_ = len_+2
                        pal = s[i-j: i+3+j]
                        j += 1
                    else:
                        break
                if len_ > len_max:
                    len_max = len_
                    longest = pal
        if i+1 < n:
            if (s[i] == s[i+1]):
                j = 0
                len_ = 2
                pal = s[i: i+2]
                while (i-j >= 0) and (i+1+j < n):
                    if s[i-j] == s[i+1+j]:
                        len_ = len_+2
                        pal = s[i-j: i+2+j]
                        j += 1
                    else:
                        break
                if len_ > len_max:
                    len_max = len_
                    longest = pal
        else:
            break
        i += 1
    return longest
