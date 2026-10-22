# 找出1000以内的强数。
# 如果一个正整数等于其各位数字的阶乘之和，则称该数为强数。
# 例如，145 = 1! + 4! + 5!
result = []
for i in range(1,1001):
    total = 0
    for char in str(i):
        x = 1
        for j in range(1, int(char) + 1):
            x = x*j
        total = total + x
    if total == i:
        result.append(i)
my_result = " ".join(map(str, result))
print(f"{my_result}是强数")


