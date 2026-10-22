m, n = map(int, input("输入两个正整数:m<n ").split(" "))
i = n
while True:
    if i % m == 0 and i % n == 0:
        print(i)
        break
    i += 1