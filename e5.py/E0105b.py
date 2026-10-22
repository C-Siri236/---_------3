num = int(input("输入1个正整数: "))
count = 0
if num == 0:
    print("1")
else:
    while num != 0:
        num = num // 10
        count += 1
print(count)