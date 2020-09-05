class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def add(num1,num2):
            if len(num2) > len(num1):
                return add(num2,num1)
            #t表示进位
            t= 0

            result =[]
            for i in range(len(num1)):
                c= t+int(num1[i])
                if i <len(num2):
                    c+=int(num2[i])
                t= c//10
                c = c%10
                result.append(str(c))
            if t :
                result.append(t)
            res = ''.join( str(i) for i in result[::-1])
            return res
        return add(num1[::-1],num2[::-1])
solution =Solution()
print(solution.addStrings('9','99'))

