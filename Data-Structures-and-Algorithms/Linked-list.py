# references:
#   https://blog.csdn.net/xutiantian1412/article/details/79619674


# example of a (single) linked list
class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkList(object):
    # create a linked list from a list
    def __init__(self, arg=None):
        # if no arg
        if arg is None:
            self.head = ListNode()
        # if arg is a ListNode
        elif isinstance(arg, ListNode):
            self.head = arg
        # if arg is iterable
        else:
            # dummy head(means we will return head.next at last)
            dummy_head = curr = ListNode()
            for item in arg:
                curr.next = ListNode(val=item)
                curr = curr.next
            self.head = dummy_head.next

    def __repr__(self):
        output = []
        curr = self.head
        while curr:
            output.append(str(curr.val))
            curr = curr.next
        return '->'.join(output)

    def __str__(self):
        return self.__repr__()


LinkList([9, 99, 999])


# reverse the linked list
# NB! this function will change the argument
def reverse(head):
    if head is None or head.next is None:
        return head
    curr = head
    prev = None
    while curr:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_
    return prev


LinkList(reverse(LinkList([9, 99, 999]).head))


# use recursion
def reverse1(head):
    if head.next is None:
        return head
    last = reverse1(head.next)
    head.next.next = head
    head.next = None
    return last
# algo:
# 1. at each recursive procedure, head is the further next node
# 2. head.next.next = head: (next of head.next) = head
# 3. head.next = None: avoid the cycle
