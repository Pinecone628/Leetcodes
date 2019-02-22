class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        count = {}
        sum = 0
        for i in s:
            count[i] = s.count(i)
        if 'I' in s:
            sum += 1 * count['I']
        if 'V' in s:
            sum += 5 * count['V']
        if 'X' in s:
            sum += 10 * count['X']
        if 'L' in s:
            sum += 50 * count['L']
        if 'C' in s:
            sum += 100 * count['C']
        if 'D' in s:
            sum += 500 * count['D']
        if 'M' in s:
            sum += 1000 * count['M']
        if 'IV' in s:
            sum -= s.count('IV') * 2
        if 'IX' in s:
            sum -= s.count('IX') * 2
        if 'XL' in s:
            sum -= s.count('XL') * 20
        if 'XC' in s:
            sum -= s.count('XC') * 20
        if 'CD' in s:
            sum -= s.count('CD') * 200
        if 'CM' in s:
            sum -= s.count('CM') * 200
        return sum

    def romanToInt2(self, s: 'str') -> 'int':
        sum = 0
        temp = 0
        t = len(s) - 1
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        while t >=0:
            if t != 0 and dict[s[t]] > dict[s[t-1]]:
                temp = dict[s[t]] - dict[s[t-1]]
                t -= 2
            else:
                temp = dict[s[t]]
                t -= 1
            sum += temp
        return sum

if __name__ == "__main__":
    ss = "CMXLVIII"
    m = Solution()
    print(m.romanToInt2(ss))
