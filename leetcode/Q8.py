# read questions clearly is very important! O(N)
def atoi(s):
    number_str = '0123456789'
    ourput_str = ''
    signal = 1
    for i in range(len(s)):
        if s[i] != ' ':
            if s[i] in '+-' + number_str:
                if s[i] == '-':
                    i += 1
                    signal = -1
                elif s[i] == '+':
                    i += 1
                for j in range(i, len(s)):
                    if s[j] in number_str:
                        ourput_str += s[j]
                    else:
                        break
                break
            else:
                break
    if ourput_str == '':
        return 0
    if int(ourput_str) * signal >= 2**31:
        return 2147483647
    if int(ourput_str) * signal < -1*2**31:
        return -2147483648
    return int(ourput_str) * signal
