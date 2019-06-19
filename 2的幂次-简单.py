#我的思路
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n ==1:
          return True
        count = 0
        tmp =n
        while tmp >=2:
            tmp = tmp//2
            count+=1
        if n-2**tmp ==0:
            return True
        else:
            return False
solution =Solution()
print(solution.isPowerOfTwo(218))

#别人的思路(常规思路)
def isPowerOfTwo(self, n: int) -> bool:
    return n >0 and 2 ** (math.log(2,n)) == n

#利用位运算,2的幂次的2进制数只有最高位是1，其余全是0.对应下面的表达式。
def isPowerOfTwo(self, n: int) -> bool:
    return n > 0 and n & (n-1) ==0