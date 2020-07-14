"""

将字符串中的空格替换成%20
eg: We are happy
->  We%20are%20happy
"""


if __name__ == "__main__":
    old = "We are happy"
    new = old.replace(' ', '%20')
    print(new)
