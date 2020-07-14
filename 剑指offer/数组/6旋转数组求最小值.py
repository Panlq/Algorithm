"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
结合两个有序数组进行二分查找

"""


class Solution(object):
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        left = 0                         # 左指针
        right = len(rotateArray) - 1     # 右指针
        mid = 0                         # 中间指针
        # 确保旋转
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:       # 左右相邻指针
                mid = right
                break
            mid = (left + right)//2  # 计算中间指针的位置
            # 特殊情况：如果无法确定中间元素是属于前面还是后面的递增子数组，只能顺序查找
            if rotateArray[left] == rotateArray[mid] and rotateArray[mid] == rotateArray[right]:
                return self.minInorder(rotateArray, left, right)
            # 中间元素位于前面的递增子数组，此时最小元素位于中间元素的后面
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            # 中间元素位于后面的递增子数组，此时最小元素位于中间元素的前面
            else:
                right = mid

        return rotateArray[mid]

    def minInorder(self, array, left, right):
        # 顺序寻找最小值
        result = array[left]
        for i in range(left+1, right):
            if array[i] < result:
                result = array[i]
        return result



