1二叉树的深度优先遍历：

（1）先序非递归：

    （1）根节点入栈
    （2）出栈一个节点，并访问。
    （3）若有孩子，则右孩子先入栈，然后左孩子入栈，循环执行，直到
    栈空为止。
    
（2）中序遍历非递归：
    
    （1）根节点入栈
    
    （2）如果栈顶节点左孩子存在，则左孩子入栈，如果栈顶节点左孩子不存在，
    则出栈并输出栈顶节点，然后检查右孩子是否存在，若存在，右孩子入栈。
    
    （3）栈空时算法结束。
    
        while top！=-1 and p!=None:
            while p ！= Null:
                stack[++top] = p
                p = p.left
            
            if top!=-1:
                p = stack[top--]
                visit(p)
                p = p.right

(3)图的深度优先遍历，邻接矩阵
    
    int visitDFS[maxSize];
    void DFS(MGraph G,int i)
    {
        int j;
        visitDFS[i] = 1;
        printf("%d ", G.Vex[i]);
        for (j = 0; j < G.vexnum; j++)
        {
            if (G.Edge[i][j] != 32767 && !visitDFS[j])
                DFS(G, j);
        }
    }
     
    void DFSTraverse(MGraph G)
    {
        int i;
        for (i = 0; i < G.vexnum; i++)
            visitDFS[i] = 0;
        for (i = 0; i < G.vexnum; i++)
        {
            if (!visitDFS[i])
                DFS(G, i);
        }
    }
    
（4）图的广度优先遍历：
    
    思想：（1）根节点入队列，然后将所有的邻接点的顶点进行遍历，如果
    还没有访问过，那么将该节点入队列，然后在出栈一个元素，重复执行上述操作。
    
（5）图中最小生成树的形成过程
 
 5.1prim算法：
    
    （1）将Vo到其他顶点的所有边当做候选边；
    
    （2）重复一下n-1次，使得其他的n-1个顶点并入到生成树中。
   
     1、从候选边中挑选权值最小的边输出，并将与改变另一端相接的顶点V
      并入生成树中
     2、考察所有剩余顶点vi,如果（V,Vi）的权值比lowcost[vi]小，
     则用（V,Vi）的权值更新。
     
5.2 克鲁斯卡尔算法

每次找出候选边中权值最小的边，将该边并入生成树中，重复该过程直到
所有边被检测完毕

（6）最短路径

6.1迪杰斯特拉算法

通常用于求图中某一顶点到其余各顶点的最短路径

算法执行过程：

    （1）从当前dist[]数组中选取最小值，假设为dist[Vu],将set[vu]设置
    为1
    （2）循环检查图中顶点，如果vj已经被并入，则什么都不做，否则比较dist[vj]
    和dist[vu]+(vu,vj)大小，赋值更小者
    
    算法复杂度为O（n^2）
    
6.2弗洛伊德算法

求图中任意一对顶点间的最短路径。

初始时需要设置两个矩阵A和Path。A用来记录两个顶点之间的最短路径的长度
，Path用来记录两顶点间最短路径要经过的中间顶点

逐个以某个顶点开始检测，是否经过该顶点后任意两个顶点间的距离会更短，如果是则更新，并将path对应
位置设置该顶点编号。

主要代码：

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][j] >A[i][k]+A[k][j]:
                    A[i][j] = A[i][k]+A[k][j]
                    path[i][j] = k
时间复杂度0（n^3）

（7）排序相关总结：

7.1堆排序：

建堆的过程，从非叶子节点的右下端开始，往左上遍历，如果该节点值小于孩子节点，则交换。

排序总结：
（1）时间复杂度：快些以nlog2n归队，快速，希尔，归并、堆排序是O（nlogn）
其他是O（n2）

（2）空间复杂度：快速排序O（logn），归并0（n）

（3）稳定性：快速，简单选择，希尔，堆排序是不稳定的，其他都是稳定的。

（8）查找总结

b树和b+树的区别：

(1)在b+树中，具有n个关键字的节点含有n个分支，而在B-树中，含有n+1个分支。

（2）在B+树中叶子节点包含信息，并且包含了全部信息，叶子节点引出的指针指向记录。

