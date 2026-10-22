# 找出1000以内的孪生素数。孪生素数是指一对素数，它们之间相差2。
# 例如，3和5，5和7，11和13等等都是孪生素数。
result = []
for i in range(2, 1001):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
            a = i + 2
            for b in range(2, a):
                if a % b == 0:
                    break
            else:
                result.append(f"{i}和{a}")
my_result = " ".join(map(str, result))
print(my_result)