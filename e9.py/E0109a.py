# 输入两个正整数，求它们的最大公约数。 
# 测试： 输入1 61，输出1 输入24 66，输出6 
result = []
m, n = map(int, input("输入两个正整数:(m < n) ").split(" "))
for i in range(1, n):
    if m % i == 0 and n % i == 0:
        result.append(i)
print(result[-1])




