"""
统计一个数字在排序数组中出现的次数。
"""

class Solution2:
    def GetNumberOfK(self, data, k):
        length = len(data)
        if length == 0:
            return 0
        first = self.GetFirstK(data, k, 0, length - 1)
        last = self.GetLastK(data, k, 0, length - 1)
        if (first != -1 and last != -1):
            return last - first + 1

        return 0

    # 递归找到第一个K
    def GetFirstK(self, data, k, begin, end):
        if begin > end:
            return -1
        midIndex = (begin + end) >> 1
        midData = data[midIndex]

        if midData == k:
            if (midIndex > 0 and data[midIndex - 1] != k) or midIndex == 0:
                return midIndex
            else:
                end = midIndex - 1

        elif midData > k:
            end = midIndex - 1
        else:
            begin = midIndex + 1
        return self.GetFirstK(data, k, begin, end)

    # 循环找到最后一个
    def GetLastK(self, data, k, begin, end):
        length = len(data)
        midIndex = (begin + end) >> 1
        midData = data[midIndex]

        while (begin <= end):
            if midData == k:
                if (midIndex < length - 1 and data[midIndex + 1] != k) or (midIndex == length - 1):
                    return midIndex
                else:
                    begin = midIndex + 1

            elif midData > k:
                end = midIndex - 1
            else:
                begin = midIndex + 1
            midIndex = (begin + end) >> 1
            midData = data[midIndex]

        return -1



class Solution:
    def GetNumberOfK(self, data, k):
        return data.count(k)



if __name__ == '__main__':
    a = [1,2,3,4,5,5,5,5,5, 6,7,8,9,10]

    print(Solution().GetNumberOfK(a, 5))
    print(Solution2().GetNumberOfK(a, 5))