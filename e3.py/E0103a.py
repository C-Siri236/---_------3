a = int(input("输入一个较小正整数："))
b = int(input("输入一个较大正整数："))
total = 0
for i in range(a,b+1):
    total = total + i
print(total)