# example of a (single) linked list


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList(object):
    # create a linklist from a list
    def __init__(self, li):
        # dummy head(means we will return head.next at last)
        dummy_head = curr = ListNode()
        for item in li:
            curr.next = ListNode(val=item)
            curr = curr.next
        self.head = dummy_head.next


test = LinkList([7, 40, 3]).head
test.val
test.next.val
test.next.next.val
