
"""
-----------
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
-----------
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

思路：
遍历列表，用target减去元素1，得到他的另外一个元素，存在字典里，
key:value key就是另一个加数， 元素2的下标记录,
然后在判断遍历的元素是否在字典里，有直接输出
"""


def twoSum(nums, target):
  """
  nums:is iterable list
  元素是整数
  """
  if len(nums) <= 1:
    return False
  buff_dict = {}
  for i in range(len(nums)):
    if nums[i] in buff_dict:
      return [buff_dict[nums[i]] + 1, i + 1]
    buff_dict[target-nums[i]] = i
      

def twoSum2(nums, target):
    # 双指针解法
    if len(nums) <= 1:
        return None

    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return i + 1, j + 1
        elif s < target:
            i += 1
        else:
            j -= 1
        
    return None
    
      
# >>>twoSum([3,2,4], 6)
# 如果判断的有重复的如[3, 2, 4, 3]  可以添加一个列表来存储满足的对象，然后在输出！


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
    print(twoSum2(nums, target))
    
