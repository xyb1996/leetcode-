class Solution(object):
	def sortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		"""肯定要用快速、归并or推排序、首先想到快速
		只不过一般的快速排序都是双向遍历、进行partition，而链表只能单向遍历，这里采用另一种遍历法
		就是从头至尾遍历，遇到大于pivot的数，只动cur游标，遇到小于pivot的数，动cur和left游标，并将cur和left进行
		交换，left游标相当于记录了上一个大于pivot的位置的前一个位置。这种排序思路貌似常见
		"""
		def swap(item1,item2):
			tmp = item1.val
			item1.val = item2.val
			item2.val = tmp
			return
		def quicksort(head,tail):
			#注意这里是tail不是None
			if head ==tail or head.next ==tail:return
			pivot = head.val
			begin = head
			cur = head.next
			#注意这里的tail是None
			while cur!=tail:
				if cur.val<pivot:
					begin=begin.next
					swap(begin,cur)
				cur =cur.next
			swap(head,begin)
			quicksort(head,begin)
			quicksort(begin.next,tail)
		quicksort(head,None)
		return head
	#上面算法跑出来显示超时，用下面的算法

class Solution2(object):
	def sortList(self, head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	def partition(start, end):
		node = start.next.next
		pivotPrev = start.next
		pivotPrev.next = end
		pivotPost = pivotPrev
		while node != end:
		#记录下一个节点
			temp = node.next
		#如果当前节点大于pivot，则将该节点插入最后
			if node.val > pivotPrev.val:
				node.next = pivotPost.next
				pivotPost.next = node
			#如果小于，则前插入之头结点后面
			elif node.val < pivotPrev.val:
				node.next = start.next
				start.next = node
			#如果相等，那么将该节点插入末尾，并且将pivot移动一个位置
			else:
				node.next = pivotPost.next
				pivotPost.next = node
				pivotPost = pivotPost.next
			node = temp
			#其实pivotPrev和pivotPost是一样的，如果有两个节点值为pivot的值才会不一样。

		return [pivotPrev, pivotPost]

	def quicksort(start, end):
		if start.next != end:
			prev, post = partition(start, end)
			quicksort(start, prev)
			quicksort(post, end)

	newHead = ListNode(0)
	newHead.next = head
	quicksort(newHead, None)
	return newHead.next



