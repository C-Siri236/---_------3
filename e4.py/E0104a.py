n = int(input("输入正整数: "))
if n == 1 or n == 2:
    print("1")
else:
    a = 1
    b = 1
    for i in range(1,n-1):
        
        a, b = b, a + b 
    
    print(b)