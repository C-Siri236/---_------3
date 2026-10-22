#  2进制转10进制
n = input("输入一个2进制数: ")
result = []
x = len(n)
a = 0
b = 1
for i in n:
    a = a + (int(i))*(2**(x-b))
    b += 1
print(a)

