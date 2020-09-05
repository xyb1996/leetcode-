# leetcode-

1、一些刷题的小小注意点，一时想不到可能会很难受

根据字典的键值排序顺序输出key，value

a = {'1':1,'10':10,'2':2}

按照字典的键的数值大小进行排序打印，如果是按字典顺序则不是map（int）了

for i in sorted(list(map(int，keys()))):

    print(i,a[i])

2、from collections import Counter，记住Counter是在collection中的

3、最大的float  float（'inf'），最大的整数位sys.maxsize

4、bisect.bisect用于查找有序数组中某元素的插入位置
