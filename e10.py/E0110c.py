# 10-16
chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
n = int(input("输入一个10进制正整数: "))
result = []
if n == 0:
    print(0)
while n > 0:
    m = n % 16
    result.append(chars[m])
    n //= 16
x = "".join(result[::-1])
print(x)