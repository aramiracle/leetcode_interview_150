class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        Detects whether a singly linked list contains a cycle using
        Floyd's Tortoise and Hare algorithm.

        Args:
            head (ListNode): The head node of the linked list.

        Returns:
            bool: True if there is a cycle in the linked list, 
                  False otherwise.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
