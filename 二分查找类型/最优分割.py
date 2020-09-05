"""
题目描述：
依次给出n个正整数A1，A2，… ，An，将这n个数分割成m段，每一段内的所有数的和记为这一段的权重，
m段权重的最大值记为本次分割的权重。问所有分割方案中分割权重的最小值是多少？

"""
#考虑如果最多可以将这n个数分割成n段，最小就先是1段吧，然后就可以开始二分查找了
#利用二分逼近法来求解：用x
def S(arr, m):
    #最小值为max（arr），即分割长度为1
    left = max(arr)
    right = sum(arr)
    while left < right:
        mid = (left + right)>>1
        sets = 1
        cur = 0
        for num in arr:
            #讲数组分段，如果分段长度大于mid，则组数+1，cur重新置为0
            if cur + num > mid:
                sets += 1
                cur = 0
            cur += num
        #如果分的集合太多，那么需要增大权重
        if sets > m:
            left = mid+1
        #否则集合可能小于等于m，需要减少权重，知道，但是可能包含right这边的情况，所以right是mid，而不是mid-1
        else:
            right = mid
    return left
import sys
lines = sys.stdin.readlines()
s = []
for line in lines:
    s.append(list(map(int,line.split())))
n, m = s[0]
arr = s[1]
print(S(arr,m))
