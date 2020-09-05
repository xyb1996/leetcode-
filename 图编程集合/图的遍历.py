#别人的思路：一共2*(n-1)条边，减去最长的一条边就是，一共遍历的路径
#这个明明是BFS啊

class Solution:
    def bfs_max(self,s,graph,paths):
        self.maxlen = 0
        def bfs(s,graph,paths):
            while len(s)>0:
                vi,w = s.pop()
                for vj in graph[vi]:
                    if paths[vj] is None:
                        paths[vj] = w+1
                        self.maxlen = max(self.maxlen,w+1)
                        s.append((vj,w+1))
        bfs(s,graph,paths)
        return self.maxlen
if __name__ == '__main__':
    vnum = int(input())
    graph = [[] for i in range(vnum+1)]
    paths = [None for i in range(vnum+1)]
    s = [(1,0)]
    paths[1] = 0
    for i in range(vnum-1):
        a,b = list(map(int,input().split(" ")))
        graph[a].append(b)
        graph[b].append(a)
    A = Solution()
    print(2*(vnum-1)-A.bfs_max(s,graph,paths))