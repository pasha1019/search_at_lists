print('Введите первый список')
a = input().split()
print('Введите второй список')
b = input().split()
print('Введите третий список')
c = input().split()
d = []
result = []
for i in a:
    for j in b:
            if i == j:
                d.append(i)
for i in c:
    for j in d:
        if i == j:
            result.append(i)
            break
print(result)
