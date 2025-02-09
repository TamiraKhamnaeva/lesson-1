"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""
my_list = input("Введите количество элементов списка через пробел: ").split(' ')
i, j = 0, 1
while len(my_list) > j:
    my_list[i], my_list[j] = my_list[j], my_list[i]
    i += 2
    j += 2

print(my_list)