'''
Note: Your solution should have O(l.length) time complexity and O(1) space complexity, since this is what you will be asked to accomplish in an interview.

Given a singly linked list, reverse and return it.

Example

For l = [1, 2, 3, 4, 5], the output should be
reverseLinkedList(l) = [5, 4, 3, 2, 1].

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ l.length ≤ 105,
-109 ≤ l.value ≤ 109.

[output] linkedlist.integer

Reversed l.
'''

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseLinkedList(l):
    cur = l
    prev = None
    
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev