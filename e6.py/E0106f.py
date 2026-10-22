# 找出1000以内的阿姆斯特朗数。
# 如果一个n位正整数等于其各位数字的n次方之和
# 例如，1^3 + 5^3 + 3^3 = 153。
# 当n=3时，又称水仙花数。
# 水仙花数共有4个，分别为：153、370、371、407。
result = []
for i in range(1,1001):
    total = 0
    for char in str(i):
        j = int(char)
        total = total + j**len(str(i))
    if total == i:
        result.append(i)
my_result = ",".join(map(str,result))
print(f"1000以内的阿姆斯特朗数有{my_result},水仙花数共有4个：153、370、371、407")           



