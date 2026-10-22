# 找出1000以内的自守数。
# 如果一个正整数的平方的尾数等于该数自身，则称该数为自守数。
# 例如，1、5、6、25、76、376、625、9376、90625都是自守数
result = []
for i in range(1,1001):
    a = str(i**2)
    b = a[-len(str(i)):]
    if b == str(i):
        result.append(i)
my_result =" ".join(map(str, result))
print(f"{my_result}是自守数")