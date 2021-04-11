# Palindrome Number
def isPalindrome(x):
    return True if str(x) == str(x)[::-1] else False
# O(1)


# Follow up: Could you solve it without converting the integer to a string?
def isPalindrome(x):
    if (x > 0 and x % 10 != 0) or x == 0:
        right = 0
        while right < x:
            right = right*10 + x % 10
            x = x // 10
        return x in [right, right//10]
    return False
# O(N), but this is faster under leetcode test
# use % and // for integer questions
# keep considering the exception cases
