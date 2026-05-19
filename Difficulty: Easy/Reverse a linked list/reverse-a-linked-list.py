"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # store next node
            curr.next = prev        # reverse link
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        return prev
        