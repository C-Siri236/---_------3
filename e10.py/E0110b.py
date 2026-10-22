# 10进制转8进制 
n = int(input("输入一个10进制正整数: "))
result = []
if n == 0:
    print(0)
while n > 0:
    m = n % 8
    result.append(str(m))
    n //= 8
x = "".join(result[::-1])
print(x)