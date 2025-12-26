# Открываем файл. Убедитесь, что файл nums.txt лежит в той же папке.
# В файле должны быть только числа (без заголовков), скопированные из Excel/задания.
try:
    with open('nums.txt') as f:
        data = [list(map(int, line.split())) for line in f]
except FileNotFoundError:
    print("Ошибка: Файл 'nums.txt' не найден. Создайте его и скопируйте туда числа.")
    exit()

n = len(data)  # строки
m = len(data[0])  # столбцы

# Создаем таблицы для динамического программирования
# Заполняем нулями
dp_min = [[0] * m for _ in range(n)]
dp_max = [[0] * m for _ in range(n)]

# Инициализируем стартовую клетку
dp_min[0][0] = data[0][0]
dp_max[0][0] = data[0][0]

for i in range(n):
    for j in range(m):
        # Если сама клетка - стена, пропускаем её
        if data[i][j] == -1:
            continue

        # Если это старт, мы его уже заполнили
        if i == 0 and j == 0:
            continue

        opts_min = []
        opts_max = []

        # Смотрим ВВЕРХ: если не край И там не стена
        if i > 0 and data[i - 1][j] != -1:
            opts_min.append(dp_min[i - 1][j])
            opts_max.append(dp_max[i - 1][j])

        # Смотрим ВЛЕВО: если не край И там не стена
        if j > 0 and data[i][j - 1] != -1:
            opts_min.append(dp_min[i][j - 1])
            opts_max.append(dp_max[i][j - 1])

        # Если есть откуда прийти (список вариантов не пуст)
        if opts_min:
            dp_min[i][j] = min(opts_min) + data[i][j]
            dp_max[i][j] = max(opts_max) + data[i][j]
        else:
            # Если прийти неоткуда (изолированная клетка), помечаем как 0
            # (но по условию задачи все натуральные клетки достижимы)
            pass

# Сбор результатов
final_vals_min = []
final_vals_max = []
count_final = 0

for i in range(n):
    for j in range(m):
        # Если клетка - стена, она не может быть финальной точкой маршрута
        if data[i][j] == -1:
            continue

        # Проверяем, можно ли идти дальше
        # Нельзя ВНИЗ, если это последняя строка ИЛИ снизу стена
        cant_go_down = (i == n - 1) or (data[i + 1][j] == -1)

        # Нельзя ВПРАВО, если это последний столбец ИЛИ справа стена
        cant_go_right = (j == m - 1) or (data[i][j + 1] == -1)

        # Если никуда нельзя — это финальная клетка
        if cant_go_down and cant_go_right:
            count_final += 1
            # Добавляем значение, если до клетки вообще можно было добраться
            # (проверка dp_min[i][j] > 0 гарантирует, что мы посетили её)
            if dp_min[i][j] > 0:
                final_vals_min.append(dp_min[i][j])
                final_vals_max.append(dp_max[i][j])

print(count_final)
print(min(final_vals_min))
print(max(final_vals_max))