# leetcode-166. 分数到小数

**题目：**给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。如果小数部分为循环小数，则将循环的部分括在括号内。[链接](https://leetcode-cn.com/problems/fraction-to-recurring-decimal)

**示例 1:**

> 输入: numerator = 1, denominator = 2
> 输出: "0.5"

**示例 2:**

> 输入: numerator = 2, denominator = 1
> 输出: "2"

**示例 3:**

> 输入: numerator = 2, denominator = 3
> 输出: "0.(6)"



### 解题思路

思路：模式消除出发，当小数部分出现重复的时候, 余数也开始重复

这种题需考虑以下情况

> 正负号问题
>
> 加小数点的情况, 比如 8/ 2 不需要加小数点
>
> 小数部分,如何判断是否开始循环了



1. 先判断结果的正负

2. 直接相除, 通过余数,看能否整除

3. 开始循环的时候, 说明之前已经出现过这个余数, 我们只要记录前面出现余数的位置,插入括号即可!

#### python版本

```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        res = ['-'] if numerator * denominator < 0 else []
        numerator, denominator = abs(numerator), abs(denominator)
        # 判断有没有小数
        a, b = divmod(numerator, denominator)  # return the tuple (x//y, x%y)
        res.append(str(a))
        if b == 0:
            return "".join(res)
        
        res.append('.')
        # 处理余数，并记录所有出现过的余数的索引，判断循环节点
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            if b in loc:
                res.insert(loc[b], "(")
                res.append(")")
                break
            loc[b] = len(res)
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.fractionToDecimal(1, 2))
    print(s.fractionToDecimal(2, 3))
    print(s.fractionToDecimal(1, 6))
    print(s.fractionToDecimal(8, 2))
```



#### golang版本

```go
package main
func main {
    
}
```

