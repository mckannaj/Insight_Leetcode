
"""
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
"""

zExtraTests = False # available if we want to do some extra tests

#constructor for a Node of singly linked list
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

import warnings
def oddEvenList_Helper(head):
    if(isinstance(head, ListNode)):
        if (head.data is None): # nothing to help with; bail
            return head
        if (head.next is None): # nothing more to help with; bail
            return head
        first_even = head.next # store the first even, so we can link the last odd to it

        pointer = head # start at the first node
        change_this = head

        idx = 1 # is this necessary? can we do it a better way?
        while pointer.next is not None:
            current_next = pointer.next # store this, so we can go here next
            change_this = pointer
            if (pointer.next.next is not None):
                change_this.next = pointer.next.next # point it at the node two away (groups odds and evens)
            pointer = current_next # move to the next node
            idx = idx + 1 # keep track to see whether we have an odd or even number in total

        if ((idx % 2) == 1): # we have an odd number of nodes; need to tack the last odd on at the end of the odd list
            change_this.next = pointer
            change_this = change_this.next

        change_this.next = first_even # put the evens at the end

        return head
    else: # not a ListNode; warn and bail
        warn_message = 'WARNING: oddEvenList_Helper expected input Listnode. Returning %s' % head
        warnings.warn(warn_message)
        return head


#DO NOT CHANGE THIS FUNCTION
def oddEvenList(head):
    return oddEvenList_Helper(head)


#test case
def main():
    if (zExtraTests == True):
        # test some edge conditions first
        head = []
        head = oddEvenList(head)
        print("Edge condition 1: not a ListNode; returning %s." % head)
        head = ListNode([])
        head = oddEvenList(head)
        print("Edge condition 2: empty ListNode; returning %s." % head)
        head = ListNode(1)
        head = oddEvenList(head)
        print("Edge condition 3: only one element; returning {}.".format(head.data))

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(6)
        head =  oddEvenList(head)
        print ("Expected result: 1, 3, 5, 2, 4, 6")
        print ("Your result is {}, {}, {}, {}, {}, {}".format(head.data, head.next.data, head.next.next.data, head.next.next.next.data, head.next.next.next.next.data, head.next.next.next.next.next.data))

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(6)
        head.next.next.next.next.next.next = ListNode(7)
        head = oddEvenList(head)
        print("Expected result: 1, 3, 5, 7, 2, 4, 6")
        print("Your result is {}, {}, {}, {}, {}, {}, {}".format(head.data, head.next.data, head.next.next.data,
                                                             head.next.next.next.data, head.next.next.next.next.data,
                                                             head.next.next.next.next.next.data, head.next.next.next.next.next.next.data))


    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head =  oddEvenList(head)
    print ("Expected result: 1, 3, 5, 2, 4")
    print ("Your result is {}, {}, {}, {}, {}".format(head.data, head.next.data, head.next.next.data, head.next.next.next.data, head.next.next.next.next.data))

if __name__ == "__main__":
    main()