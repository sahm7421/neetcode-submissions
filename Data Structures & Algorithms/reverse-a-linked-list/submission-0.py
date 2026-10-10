# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next  # agle node ka reference save karo
            curr.next = prev  # pointer ko ulta ghuma do
            prev = curr  # prev ko ek kadam aage badhao
            curr = nxt  # curr ko agle node par le jao

        return prev