# 找出1000以内的回文数。从左向右和从右向左读都是一样的整数。
# 例如，121是回文数，而123不是
my_list = []
for i in range(1, 1001):
    j = str(i)
    a = j[::-1]
    b = "".join(a)
    if int(b) == i:
        my_list.append(i)
print(my_list)        