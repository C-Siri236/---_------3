n = int(input("输入正整数: "))
my_list = [1,1]
if n == 1 or n == 2:
    print("1")
else:
    a = 1
    b = 1
    for i in range(2, n-1):
        a, b = b, a + b
    my_list.append(a + b)
print(my_list[-1])    