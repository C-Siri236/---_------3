# 求1000以内的亲和数。
# 指两个正整数中，彼此的全部真因子（本身除外的所有因子）之和与另一方相等。
# 例如，220和284、1184 和1210、2620和2924、5020 和5564、6232和6368。
for i in range(1, 1001):
    a = 0
    for j in range(1, i//2 + 1):
        if i % j == 0:
            a += j
    if a > 1000 or a == i:
        continue
    else:
        b = 0
        for k in range(1, a//2 + 1):
            if a % k == 0:
                b += k
    if b == i and i < a:
        print(f"{i}和{a}是亲和数")
        

        
        
                

