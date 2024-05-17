# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.


class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head_list = head
        counter = 1

        while head_list.next:
            counter += 1
            head_list = head_list.next


        middle = int(counter / 2)
        node = ListNode(0, None)
        i = 0
        while i < counter:

            if i == middle:
                node.val = head.val
                node.next = head.next
                i += 1
                head = head.next
                break
            else:
                i += 1
                head = head.next

        return print(node)

Solution().middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,))))))

# Equivalent to the following Python code:

class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

print(Solution().middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))




