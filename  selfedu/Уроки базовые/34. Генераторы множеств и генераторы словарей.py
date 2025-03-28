"""Генератор списков (для напоминания)"""
a = [x ** 2 for x in range(1, 5)]
print(a)  # [1, 4, 9, 16]
"""Генератор множества"""
b = {x ** 2 for x in range(1, 5)}  # тоже самое, что и список, только фигурные скобки вместо квадратных
print(b)  # {16, 1, 4, 9} - это множество, а не словарь, т.к. нет ключей
"""Генератор словаря"""
c = {x: x ** 2 for x in range(1, 5)}
print(c)  # {1: 1, 2: 4, 3: 9, 4: 16} это словарь, т.к. есть ключи

"""Применение. Для преобразования списка в множество, состоящее только из чисел"""
d = [1, 2, '1', '6', -4, 3, 4]
e = {int(x) for x in d}  # Строка '6' перешло в int
print(e)  # {1, 2, 3, 4, 6, -4}
"""Будет работать гораздо медленнее, если делать через цикл ниже"""
set_e = set()
for x in d:
    set_e.add(int(x))
print(set_e)  # {1, 2, 3, 4, 6, -4}
"""Аналогично со словарем. Задача: Ключи написать заглавными буквами, а значения преобразовать в числа"""
f = {'неудовл.': 2, 'удовл.': 3, 'хорошо': '4', 'отлично': '5'}
g = {key.upper(): int(value) for key, value in f.items()}
print(g)  # {'НЕУДОВЛ.': 2, 'УДОВЛ.': 3, 'ХОРОШО': 4, 'ОТЛИЧНО': 5}
"""Задача: список d преобразовать в множество, состоящее только из положительных чисел"""
h = {int(x) for x in d if int(x) > 0}
print(h)

"""Генератор словаря с условием. 
Задача: в словаре k поменять местами ключ и значение и выбрать оценки от 2 до 5"""
k = {'безнадежно': 0, 'убого': 1, 'неудовл.': 2, 'удовл.': 3, 'хорошо': '4', 'отлично': '5'}
l = {value: key for key, value in k.items() if 2 <= int(value) <= 5}
print(l)  # {2: 'неудовл.', 3: 'удовл.', '4': 'хорошо', '5': 'отлично'}
