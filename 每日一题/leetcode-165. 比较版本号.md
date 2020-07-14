##  leetcode165. 比较版本号

![img](https://windliang.oss-cn-beijing.aliyuncs.com/165.png)

## 解题思路

- **方法一**：先按【点】进行切割版本号，得到一个数组，这里要考虑数组不等长的问题，所以短的要进行补`0`操作，然后依次多数组中元素进行比较，当然字符串要转换为整数在进行比较

- **方法二**：不切割，使用双指针逐步进行比较，根据点做为前置条件，每个字符转为 ASCII 码，**并用`*10`来避免前导零和后置零的问题**， **双指针步进法 直接对字符串进行操作，这也是处理大数运算的时候的方法。**



## python版

```python
# 方法一
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        n1, n2 = len(ver1), len(ver2)

        # compare versions
        for i in range(max(n1, n2)):
            i1 = int(ver1[i]) if i < n1 else 0
            i2 = int(ver2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        # the versions are equal 
        return 0
```

**复杂度：**

- 时间复杂度： O(N + M + Max（N+M）)  N, M表示字符串长度
- 空间复杂度：O(N + M)，使用了两个数组 `ver1` 和 `ver2` 存储两个字符串的块

```python
# 方法二
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1, p2 = 0, 0
        len1, len2 = len(version1), len(version2)
        end = max(len1, len2)
        while (p1 < end or p2 < end):
            v1, v2 = 0, 0
            while (p1 < len1 and version1[p1] != '.'):
                v1 = v1 * 10 + ord(version1[p1]) - 48   # '0' Asiico = 48
                p1 += 1
            
            while (p2 < len2 and version2[p2] != '.'):
                v2 = v2 * 10 + ord(version2[p2]) - 48
                p2 += 1

            if v1 != v2:
                return 1 if v1 > v2 else -1
        
            p1 += 1
            p2 += 1

        return 0
```

**复杂度：**

- 时间复杂度： O(Max（N+M）)  N, M表示字符串长度
- 空间复杂度：O(1)，没有使用额外的数据结构



## golang版本

```golang
// If (a > b ? a : b).(type)
func If(condition bool, trueVal, falseVal interface{}) interface{} {
	if condition {
		return trueVal
	}
	return falseVal
}

func compareVersion(version1 string, version2 string) int {
	p1, p2 := 0, 0
	len1, len2 := len(version1), len(version2)
	end := If(len1 > len2, len1, len2).(int)
	for p1 < end || p2 < end {
		var v1, v2 int
		for p1 < len1 && version1[p1] != '.' {
			v1 = v1*10 + int(version1[p1]-'0')
			p1++
		}

		for p2 < len2 && version2[p2] != '.' {
			v2 = v2*10 + int(version2[p2]-'0')
			p2++
		}

		if v1 > v2 {
			return 1
		} else if v1 < v2 {
			return -1
		}

		p1++
		p2++
	}
	return 0
}
```

### go中用到的相关知识点复习

#### 字符转数字

> 组成每个字符串的元素叫做“字符”，可以通过遍历或者单个获取字符串元素获得字符。 字符用单引号（’）包裹起来

Go语言的字符有两种形式

- uint8类型， 或者叫byte型，代表ASCII码对应的字符
- rune类型，表示一个UTF-8字符，rune实际是一个int32， Go 使用了特殊的 rune 类型来处理 Unicode

字符串底层是一个byte数组，所以可以和`[]byte`类型相互转换。字符串是不能修改的 字符串是由byte字节组成，所以字符串的长度是byte字节的长度。 rune类型用来表示utf8字符，一个rune字符由一个或多个byte组成。

```go
var c rune='a' 
var i int =98
i1:=int(c)
fmt.Println("'a' convert to",i1)
c1:=rune(i)
fmt.Println("98 convert to",string(c1))

//string to rune
for _, char := range []rune("世界你好") {
    fmt.Println(string(char))
}
```

#### 字符串的修改

要修改字符串，需要先将其转换成`[]rune`或者`[]byte`，修改完成后再转换为`string`,无论哪种转换，都会重新分配内存，并复制字节数组。

```golang
func changeString() {
	s1 := "big"
	// 强制类型转换
	byteS1 := []byte(s1)
	byteS1[0] = 'p'
	fmt.Println(string(byteS1))
	
	s2 := "中文"
	runeS2 := []rune(s2)
	runeS2[1] = "国"
	fmt.Println(string(runeS2))
}
```



### go实现三元运算符

go语言没有三元运算符的表达式，为什么要去写这个三元运算符，也是因为go中没有`min\max`这个常用的函数，golang中有`math.Max(float64, float64) float64`是对float64类型的比较，由于float64类型要处理infinity和not-a-number这种值，而他们的处理非常复杂，一般用户没有能力，所有go需要为用户提供系统级别的解决办法。

- 因为Go不支持运算符重载，因此需要先将 `a<b` 在函数外转换为 `bool` 条件
- Go不支持泛型，只能用 `interface{}` 模拟
- 返回的类型安全需要用户自己保证，`.(type)` 的类型必须匹配
- `interface{}` 是运行时泛型，性能没有编译时泛型高

![image.png](https://i.loli.net/2020/06/10/nozeFigQItAH4v3.png)

>  golang还是有优势呀