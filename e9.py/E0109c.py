# 输入两个正整数，求它们的最小公倍数。
m, n = map(int, input("输入两个正整数:m<n ").split(" "))
for i in range(n, 0, -1):
    if m % i == 0 and n % i == 0:
        a = m // i
        b = n // i
        print(f"最小公倍数是{i*a*b}")
        break
