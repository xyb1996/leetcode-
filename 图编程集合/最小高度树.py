"""
问题描述：

对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，
具有最小高度的树被称为最小高度树。给出这样的一个图，写出一个函数找到所有的最小高度树并返回他们的根节点。

"""
#思路：对于邻接边只有1的边将其加入队列中，开始循环，将他的邻接边的边集合减去这个点，然后判断该邻接点只有只有一条边，是的化
#将其加入下一轮的队列中，继续判断，然后n-1，知道n《=2为止。
#就是top排序思想
import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        e = collections.defaultdict(set)        #字典初始化为集合
        for i, j in edges:
            e[i] |= {j}                         #把边哈希化，方便调用
            e[j] |= {i}
        q = {i for i in e if len(e[i]) == 1}    #建立初始宽搜队列，长度为1时代表只连接一个点
        while n > 2:
            t = set()                   #临时队列
            for i in q:
                j = e[i].pop()          #把连接点取出,因为q中的点都只有一条边，所以肯定只要一次pop，并且只有一个e[j]需要－1
                e[j] -= {i}             #连接是双向的，所以要删除关系
                if len(e[j]) == 1:      #更新后，如果长度为1时则加入下一个轮队列
                    t |= {j}
                n -= 1                  #删除计数
            q = t
        return list(q)

