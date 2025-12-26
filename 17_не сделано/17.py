# Читаем все числа в список
f = open('17_input.txt')
data = [int(x) for x in f]

ans = []  # Сюда будем сохранять нужные суммы

for i in range(len(data) - 1):
    a = data[i]
    b = data[i + 1]

    # Условие 1: ровно один имеет остаток 17 при делении на 80
    c1 = (a % 80 == 17)
    c2 = (b % 80 == 17)

    # Условие 2: оба кратны 7
    if (c1 + c2 == 1) and (a % 7 == 0 and b % 7 == 0):
        # Если условие выполнено, сохраняем число с остатком 17
        if c1:
            ans.append(a)
        else:
            ans.append(b)

print(len(ans), sum(ans))