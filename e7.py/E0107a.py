# 求100000以内素数的个数
# 题目里给错了吧？1不是素数，只有9592个...
result = []
for i in range(2,100001):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        result.append(i)
my_result = " ".join(map(str, result))
print(f"100000以内有{len(result)}个素数")