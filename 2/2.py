# Заголовок для удобства
print("x y z w | F")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # Выражение: x И (z -> w) И НЕ y
                # В Python импликация (a -> b) заменяется на (a <= b)
                f = x and (z <= w) and (not y)

                # Обычно в таких задачах дают фрагмент, где F = 1
                if f == 1:
                    print(x, y, z, w, "|", int(f))