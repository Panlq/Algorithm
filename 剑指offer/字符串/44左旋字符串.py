
"""
Q:输入字符串"abcdefg"和数字2，该函数将返回左旋转2位得到的结果"cdefgab"
S: 
1. 剑指offer: 把abcdefg 分成两部分, 由于想把它的前两个字符转移到后面，
前两个字符作为第一部分，后面的所有字符分为第二部分, 先分别翻转这两部分得到“bagfedc
然后再翻转整个字符串--> cdefgab
2. 使用偏移量位移
"""

def rotateLeft(s:'str', n:'int')->'str':
    res = []
    lens = len(s)
    if n < 0 or lens == 0:
        return s
    if n > lens:
        n = n % lens
    for i in range(lens):
        index = i + n
        if index >= lens:
            index -= lens
        res.append(s[index])
    return ''.join(res)


def rotateLeftString(s, n):
    length = len(s)
    if n <= 0 or length == 0:
        return s
    if n > length:
        n = n % length
    return s[n:] + s[:n]

if __name__ == '__main__':
    s = 'abcdefg'
    print(rotateLeft(s, 2))
    print(rotateLeftString(s, 9))
