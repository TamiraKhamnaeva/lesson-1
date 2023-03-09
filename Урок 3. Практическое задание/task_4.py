"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""
def my_func(x, y):
    try:
        if y < 0:
            res = 1
            for i in range(y,0):
                res = res * x
            res = 1 / res
            return f'Для значений x = {5}, y = {-3} результат: {res}'
        else:
            return "Число y должно быть отрицательным"

    except TypeError:
        return "Вводить только числа"
    except ZeroDivisionError:
        return "Деление на 0!"

print(my_func(5, -3))

