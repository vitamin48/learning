"""
Механизм инкапсуляции
attribute - public - доступ везде
_attribute - protect - для обращения внутри класса и во всех дочерних классах (доступ можно получить, но будет
сигнализация об этом)
__attribute - private - для обращения только внутри класса (доступ извне будет закрыт)

В Python нет жёстких ограничений на доступ к атрибутам, но есть рекомендации (по соглашению разработчиков). Они
помогают лучше организовать код и защитить данные.

Геттер (getter) – метод, который возвращает значение приватного атрибута.
Сеттер (setter) – метод, который изменяет значение приватного атрибута с проверкой.
⚡ Зачем нужны геттеры и сеттеры?
- Позволяют контролировать доступ к данным
- Позволяют проверять корректность значений
- Упрощают поддержку кода
"""


class Point:
    def __init__(self, x=0, y=0, z=0):
        if self.__check_value(x) and self.__check_value(y) and self.__check_value(z):
            self.x = x  # public
            self._y = y  # protect
            self.__z = z  # private

    @classmethod  # Есть смысл сделать этот приватный метод методом класса, т.к. он может обращаться к атрибутам класса
    def __check_value(cls, x):
        """Приватный метод проверки"""
        return type(x) in (int, float)

    def set_coord(self, x, y, z):
        if self.__check_value(x) and self.__check_value(y) and self.__check_value(z):
            """Сеттер помимо того, что обновляет приватные свойства класса, он еще производит проверку типа данных"""
            self.x = x
            self._y = y
            self.__z = z
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coord(self):
        return self.x, self._y, self.__z


"""x - public, y - protect (ошибки нет, но есть предупреждение), z - private (при попытке доступа будет ошибка)
Это делается с целью невозможности изменения защищенных данных (например, чтобы вместо числа не пришел текст)"""
pt = Point(1, 2, 3)
print(pt.x)  # 1
print(pt._y)  # 2 (есть предупреждение)
# print(pt.__z)  # AttributeError: 'Point' object has no attribute '__z'

"""Также работает и с методами внутри класса. В нашем примере это установка и получение координат"""
pt.set_coord(5, 6, 7)
print(pt.get_coord())  # (5, 6, 7)

"""Методы set_coord и get_coord - это интерфейсные методы или сеттеры и геттеры. Они служат для взаимодействия, чтобы
случайно или намеренно не нарушить целостность работы алгоритмов внутри класса. В этом СУТЬ ИНКАПСУЛЯЦИИ.
Пример с автомобилем. При езде мы используем условно руль и педали, но не вмешиваемся при движении в работу двигателя"""

"""Приватное значение всё же можно получить через кодовое значение _Point__z. Делать так крайне не рекомендуется."""
print(pt._Point__z)  # 7
"Если нужно более надежно защитить, то используется дополнительный модуль accessify"