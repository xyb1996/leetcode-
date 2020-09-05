class Solution:
    #思想就是先建立每个节点的父节点的映射，然后得到两个查询节点到根节点的链表，
	#后面就是寻找两个链表的相遇节点了。寻找第一个相遇节点问题，就是走完我这个链表后
	#走第二个人的链表，这样会在公共节点处相遇。

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic={root:None}
        def bfs(node):
            if node:
                if node.left:dic[node.left]=node
                if node.right:dic[node.right]=node
                bfs(node.left)
                bfs(node.right)
        bfs(root)
        l1,l2=p,q
        while(l1!=l2):
            l1=dic.get(l1) if l1 else q
            l2=dic.get(l2) if l2 else p
        return l1

