# 输入一个10进制正整数，输出它的2进制表示。 
# 测试： 输入：5，输出：101 
#       输入：23，输出：10111 
n = int(input("输入一个10进制正整数: "))
result = []
if n == 0:
    print(0)
while n > 0:
    m = n % 2
    result.append(str(m))
    n //= 2
x = "".join(result[::-1])
print(x)
