from itertools import product # еще может пригодиться permutations(alf, n)

# Алфавит в алфавитном порядке: А, Г, И, Н, Р, Т
alf = 'АГИНРТ'
cnt = 0

# Генерируем все варианты длины 6
for s in product(alf, repeat=6):
    cnt += 1  # Номер слова в списке

    # Условие 1: не начинается с А, И или Г
    if s[0] not in 'АИГ':
        # Условие 2: ровно одна буква А
        if s.count('А') == 1:
            # Условие 3: нечетный номер
            if cnt % 2 != 0:
                print(cnt)
                break