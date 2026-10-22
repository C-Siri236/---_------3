# 输入1个正整数，输出它的所有因子。
# 输入：220，输出：1 2 4 5 10 11 20 22 44 55 110 220 
# 输入：284，输出：1 2 4 71 142 284
result = []
n = int(input("输入1个正整数: "))
for i in range(1, n+1):
    if n % i == 0:
        result.append(i)
my_result = " ".join(map(str, result))
print(my_result)