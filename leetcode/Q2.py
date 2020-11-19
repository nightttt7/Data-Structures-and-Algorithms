class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    # l1 and l2 are special ListNode from question
    # use .next() to get next node
    # carry: save the '>10' information
    carry = 0
    # dummy head
    # (means we will delete this head at last)
    # (we return head.next but not head)
    curr = ListNode()
    head = curr
    # over the head
    # end of l1 or l2 are None
    while l1 or l2:
        val = carry
        if l1:
            val = val+l1.val
            l1 = l1.next
        if l2:
            val = val+l2.val
            l2 = l2.next
        curr.next = ListNode(val=val % 10)
        curr = curr.next
        # interesting, // here will be escaped to / in some webs
        carry = val // 10
    if carry > 0:
        curr.next = ListNode(val=carry)
    return head.next
# Time complexity: O(max(m, n))
# Space complexity: O(max(m,n))
# learned from github.com/qiyuangong/leetcode


# test
l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=9)))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
# l1 = ListNode(val=6)
# l2 = ListNode(val=5)
lsum = addTwoNumbers(l1, l2)
lsum.val
lsum.next.val
lsum.next.next.val
lsum.next.next.next.val
