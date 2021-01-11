import random
lotto = []
while len(lotto) != 6:
    a = random.randint(1, 45)
    if a not in lotto:
        lotto.append(a)
print('행운의 로또번호 : ', end='')
print(*lotto, sep=', ')

# 리스트의 요소들을 괄호 없이 나열하는 다른 방법
# for i in range(len(lotto)):
#     print(lotto[i],end='')
#     if i<len(lotto)-1:
#         print(', ',end='')
