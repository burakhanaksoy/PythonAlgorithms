# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        s1 = []
        s2 = []
        try:
            s1.append(l1.val)
        except:
            pass

        while l1.next != None:
            l1 = l1.next
            s1.append(l1.val)

        try:
            s2.append(l2.val)
        except:
            pass

        while l2.next != None:
            l2 = l2.next
            s2.append(l2.val)

        sorted_list = sorted(s1+s2)

        point = head = ListNode()
        for k in sorted_list:
            point.next = ListNode(k)
            point = point.next
        return head.next


solution_object = Solution()
solution_object.mergeTwoLists([1, 2, 4], [1, 3, 4])
