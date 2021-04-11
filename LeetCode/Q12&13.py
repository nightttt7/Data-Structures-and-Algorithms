# Integer to Roman, O(n)
def intToRoman(num):
    def radix_list(x, d):
        x_str = str(x)
        output = [0]*d
        for i, c in enumerate(reversed(x_str)):
            output[-i-1] = int(c)
        return output
    digital = {}
    digital[1] = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    digital[2] = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    digital[3] = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    digital[4] = ['', 'M', 'MM', 'MMM']
    s = ''
    i = 4
    for d in radix_list(num, 4):
        s += digital[i][int(d)]
        i -= 1
    return s


# Roman to Integer, O(n)
def romanToInt(s):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I':1}
    num = 0
    for i in range(len(s)-1):
        if roman[s[i]] < roman[s[i+1]]:
            num -= roman[s[i]]
        else:
            num += roman[s[i]]
    return num + roman[s[-1]]
