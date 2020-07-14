"""
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 
数值为0或者字符串不是一个合法的数值则返回0
"""

def strToInt(s):
    length = len(s)
    if length == 0:
        return 0
    else:
        minus = False
        flag = False
        if s[0] == '+':
            flag = True
        if s[0] == '-':
            flag = True
            minus = True
        begin = 0
        if flag:
            begin = 1
        num = 0
        minus = -1 if minus else 1
        for each in s[begin:]:
            if each >= '0' and each <= '9':
                num = num * 10 + minus * (ord(each) - ord('0'))
            else:
                num = 0
                break
        return num


if __name__ == '__main__':
    print(strToInt('0125421'))