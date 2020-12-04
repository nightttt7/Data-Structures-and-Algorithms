# Regular Expression Matching


# 1. recursion
def isMatch(s, p):
    # base case, if p is None, s is None, return True
    #            if p is None, s is not None, return False
    if not p:
        return not s

    # check the first char in p and s are the same

    # (6 lines below rewrite to 1 line)
    # if not s:
    #     first_match = False
    # elif p[0] in {s[0], '.'}:
    #     first_match = True
    # else:
    #     first_match = False

    # 1 line
    first_match = bool(s) and p[0] in {s[0], '.'}

    # when * is after
    if len(p) >= 2 and p[1] == '*':

        # (10 lines below rewrite to 1 line)
        # # assume * here means repeat 0, if rest part match
        # # even first_match is False, still return True
        # if isMatch(s, p[2:]):
        #     return True
        # # assume * here means repeat 1, if rest part match, return True
        # # as a recursion, cases repeat more than 1 also considered
        # if first_match and isMatch(s[1:], p):
        #     return True
        # else:
        #     return False

        # 1 line
        return isMatch(s, p[2:]) or first_match and isMatch(s[1:], p)

    # when not * after, if first char in p and s match
    # and the rest part in p and s match, return True
    else:
        # NB! in recursion, check others and then get into recursion
        # or "maximum recursion depth exceeded"
        # so first_match must before isMatch()
        return first_match and isMatch(s[1:], p[1:])


# 2. Dynamic Programming
def isMatch(s, p):
    # TBC
    pass
