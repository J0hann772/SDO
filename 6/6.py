# Описываем границы первого прямоугольника
x1_min, x1_max = 0, 20
y1_min, y1_max = 0, 33

# Описываем границы второго прямоугольника
# Начало в (9, 3), размеры 25 на 24
x2_min, x2_max = 9, 9 + 25
y2_min, y2_max = 3, 3 + 24

count = 0

# Перебираем область с запасом
for x in range(-10, 50):
    for y in range(-10, 50):
        # Проверяем строгое вхождение (не на границах)
        in_r1 = (x1_min < x < x1_max) and (y1_min < y < y1_max)
        in_r2 = (x2_min < x < x2_max) and (y2_min < y < y2_max)

        if in_r1 and in_r2:
            count += 1

print(count)