# references:
#   https://runestone.academy/runestone/books/published/pythonds/BasicDS/toctree.html


from copy import deepcopy


# stack, queue, deque, list

# stack: LIFO, last-in first-out
# .append and .pop
# Balanced Parentheses
# return True if the parentheses (no brackets and braces) are balanced


def par_check(string):
    par_stack = []
    for x in string:
        if x == '(':
            par_stack.append(x)
        elif x == ')':
            if not par_stack:
                return False
            else:
                par_stack.pop()
    return True if not par_stack else False


# Balanced Symbols
# return True if the symbols(parentheses, brackets, braces) are balanced


def symbol_check_1(string):
    symbol_stack = []
    for x in string:
        if x in '([{':
            symbol_stack.append(x)
        for left, right in ('()', '[]', '{}'):
            if x == right:
                if not symbol_stack:
                    return False
                elif symbol_stack[-1] == left:
                    symbol_stack.pop()
    return True if not symbol_stack else False


def symbol_check_2(string):
    match = {')': '(', ']': '[', '}': '{'}
    symbol_stack = []
    for x in string:
        if x in '([{':
            symbol_stack.append(x)
        elif x in ')]}':
            if not symbol_stack:
                return False
            elif symbol_stack[-1] == match[x]:
                symbol_stack.pop()
    return True if not symbol_stack else False


# queue: FIFO, first-in first-out
# .insert(0, ) and .pop(): in to start, out from end
# or .append() and .pop(0): in to end, out from start
# Hot Potato: children line up in a circle and pass an item from neighbor to
# neighbor as fast as they can. At a certain point in the game, the action is
# stopped and the child who has the item (the potato) is removed from the
# circle.
# use queue generate a circle
name_list = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
num = 7


def hot_potato(name_list, num):
    name_list = deepcopy(name_list)
    name_list.reverse()
    while len(name_list) > 1:
        for i in range(num-1):
            name_list.insert(0, name_list.pop())
        name_list.pop()
    return name_list


def hot_potato_recursion(name_list, num):
    if len(name_list) <= 1:
        return name_list
    for i in range(num-1):
        name_list.append(name_list.pop(0))
    name_list.pop(0)
    return hot_potato_recursion(name_list, num)


# deque: add_front, add_rear, remove_front, remove_rear

# list: each item holds a relative position with respect to the others
# Unordered List: Linked Lists (see Linked-list.py)
# Ordered List: Ordered Linked Lists
class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def add_odered(item, head):
    curr = head
    while curr.next and item > curr.val:
        curr = curr.next
    if item > curr.val:
        curr.next = ListNode(val=item, next=curr.next)
    else:
        curr.next = ListNode(val=curr.val, next=curr.next)
        curr.val = item
