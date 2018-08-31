class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode( head):
        """
        this finds the middle node of a linked list, but changes the 
        list itself by deleting trailing nodes
        """
        def findMid(newHead):
        	if newHead.next == None:
        		return newHead
        	elif newHead.next.next == None:
        		return newHead.next
        	else:
        		cursor = newHead
        		while cursor.next.next != None:
        			cursor = cursor.next
        		cursor.next = None

        		return findMid(newHead.next)

        return findMid(head)

newHead = ListNode(1)
newHead.next = ListNode(2)
newHead.next.next = ListNode(3)
#newHead.next.next.next = ListNode(4)
middle = Solution.middleNode(newHead)
print(middle.val)