class Solution:
    def reverse(self, x: 'int') -> 'int':
        if x == 0:
            return 0
        else:
            maxint = 2147483649
            minint = -2147483648
            rev = int(str(abs(x))[::-1])
            if minint < rev < maxint:
                return rev*(abs(x)//x)
            else:
                return 0