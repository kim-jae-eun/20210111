a = [[10, 20, 30, 40, 50], [5, 10, 15], [11, 22, 33, 44], [9, 8, 7, 6, 5, 4, 3, 2, 13]]
for i in range(len(a)):
    num = 0
    for j in a[i]:
        num += j
    print(i + 1, '행의 합은 ', num, ' 입니다.', sep='')

# for j in range(len(a)):
#     print(j + 1, '행의 합은 ', sum(a[j]), ' 입니다.', sep='')