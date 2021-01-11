a = [['B', 'C', 'A', 'A'], ['C', 'C', 'B', 'B'], ['D', 'A', 'A', 'D']]
b, c = ['A', 'B', 'C', 'D'], []
for i in b:
    sum = 0
    for j in range(len(a)):
        sum += a[j].count(i)
    c.append(sum)
for i in range(4):
    print(b[i], ' 는 ', c[i], '개 입니다.', sep='')