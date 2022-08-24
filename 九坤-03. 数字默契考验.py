"""
    1. 求最大公约数的辗转相除法gcd
    2. 求一个数组的最小公倍数与最大公约数都是先求前两个，然后求该最小公倍数/最大公约数与下一个数的最小公倍数/最大公约数，以此类推
    3. 求最大公约数在每个数除最大公约数相除并不可行，原因是会有子公因数乘了多次
    ps:该版本时间复杂度没过
"""


class Solution:
    def minOperations(self, numbers: List[int]) -> int:
        def gcd(a,b):
            while(a):
                tmp = a
                a = b%a
                b = tmp
            return b
        if len(numbers) == 1:
            return 0
        count = 0
        k = gcd(numbers[0],numbers[1])
        l = numbers[0]*numbers[1]/k
        for i in range(2,len(numbers)):
            k = gcd(l,numbers[i])
            l = l*numbers[i]/k
            
        for i in range(len(numbers)):
            t = l/numbers[i]
            
            while(t % 3 == 0):
                t /= 3
                count+=1
            while(t % 2 == 0):
                t/=2
                count+=1
            
            if t!=1:
                return -1
            
        return count