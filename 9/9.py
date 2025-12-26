# Читаем данные из файла (предположим, файл сохранен как txt или csv)
f = open('9-264.txt')
count = 0

for s in f:
    # Превращаем строку в список целых чисел
    a = [int(x) for x in s.split()]

    # 1. Проверка порядка убывания
    # Сравниваем список с его отсортированной версией (от большего к меньшему)
    # Если числа должны быть строго убывающими, используем set,
    # но обычно в ЕГЭ это просто a == sorted(a, reverse=True)
    cond1 = a == sorted(a, reverse=True)

    # 2. Считаем четные и нечетные
    even = 0
    odd = 0
    for x in a:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1

    cond2 = even < odd

    if cond1 and cond2:
        count += 1

print(count)