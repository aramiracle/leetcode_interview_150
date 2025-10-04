class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Merge two sorted linked lists into a single sorted linked list.

        Args:
            list1 (Optional[ListNode]): Head node of the first sorted linked list.
            list2 (Optional[ListNode]): Head node of the second sorted linked list.

        Returns:
            Optional[ListNode]: Head node of the merged sorted linked list.
        """
        sorted_list = ListNode()
        current = sorted_list
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return sorted_list.next
