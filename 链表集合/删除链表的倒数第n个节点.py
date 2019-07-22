class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		if head ==None:return head

		p1= p2 = head
		for i in range(n):
			p2 = p2.next
		if p2 ==None:
			head = head.next

		else:
			while  p2.next!=None:
				p2 = p2.next
				p1 = p1.next
			p1.next = p1.next.next
		return head