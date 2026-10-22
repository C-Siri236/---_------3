# 找出1000以内的哈沙德数。
# 如果一个正整数能够被其各个数位上的数字之和整除，
# 例如，12 是哈沙德数，
# 因为其各个数位上的数字之和为1+2=3，12能被3整除。
result = []
for i in range(1,1001):
    total = 0
    for char in str(i):
        total = total + int(char)
    if i % total == 0:
        result.append(i)
my_result = ",".join(map(str, result))
print(f"1000以内的哈沙德数{my_result}")