import random
a = set()
while len(a) != 6:
    a = a | {random.randint(1, 45)}
print('행운의 로또번호 :', end=' ')
print(*a, sep=', ')

# 집합의 원소들을 괄호 없이 나열하는 다른 방법
# j = 0
# for i in a:
#     print(i, end='')
#     if j < len(a) - 1:
#         print(', ', end='')
#         j += 1
