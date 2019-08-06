1、在一个已经排好序的数组中进行二分查找时，可以使用bisect.bisect，它将返回可以插入的位置
下标，用bisect.insort插入新元素则可以用来插入。bisect.leftinsort如果出现相等的元素，
插在相等元素的左边，rightinsort也是类似的。

2、在进行递归函数的时候注意全局变量的有效性问题，好像是数组可以直接访问
但是变量的话要在递归函数前面加上global关键字




3、常用的一些技巧总结：滑动窗口法遍历时复小，想不出来就用暴力求解法，能通过部分。

4、条件推导式：
[exp1 if condition else exp2 for x in data]，这个一直忘记了。

