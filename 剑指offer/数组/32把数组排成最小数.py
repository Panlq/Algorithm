"""
Q:输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
S:

"""


def solution(numbers):
    if len(numbers) == 0:
        return ''
    strs = list(map(str, numbers))
    cmp = lambda x, y: x > y
    compare = lambda a, b: cmp(a + b, b + a)
    # min_s = sorted(strs, cmp=compare)
    strs.sort(cmp=compare)
    return ''.join(min_s).lstrip('0')


if __name__ == '__main__':

    arr = [3, 32, 321]
    solution(arr)