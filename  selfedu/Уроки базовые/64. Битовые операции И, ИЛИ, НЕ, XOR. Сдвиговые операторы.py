"""
НЕ (инверсия бит)
0 -> 1
1 -> 0
"""
a = 121
print(bin(a))  # 0b1111001
"""Если нужно проинвертировать"""
print(~a)  # -122 (т.к. любое число кодируется набором бит 000000000 00000000 ... 00000000 .
# Старший бит (самый левый) это знаковый бит. Если 0 - число положительное, 1 - отрицательное.
# Когда мы инвертируем все биты, то получаем 11111111 11111111 ... 11111111 и это эквивалент десятичного числа -1.
# Т.е. число уменьшилось на 1 и стало отрицательным
b = 0
print(~b)  # -1
c = -10
print(~c)  # 9

"""
И (применяется уже к 2 операндам) &
0 0 -> 0
0 1 -> 0
1 0 -> 0
1 1 -> 1
"""
flags = 5
mask = 4
res = flags & mask
print(res)  # 4 т.к. 5 = 00000101, 4 = 00000100. Применяем правило И, получаем 00000100, т.е. 4.
"""Это применяется для проверки, например, включен ли второй бит у переменной flags
Также может применяться для выключения бита, например"""
flags2 = 13
mask2 = 5
flags2 = flags2 & ~mask2
print(flags2)  # 8, т.к.
# 13 = 00001101,
# 5 = 00000101,
# ~5 = 11111010 в итоге
# 8 = 00001000

"""
ИЛИ
0 0 -> 0
0 1 -> 1
1 0 -> 1
1 1 -> 1
|
Применяется обычно тогда, когда нужно включить отдельные биты переменной
"""

flags3 = 8
mask3 = 5
flags3 = flags3 | mask3
print(flags3)  # 13, т.к.
# 8 = 00001000,
# 5 = 00000101,
# 13 = 00001101

"""
XOR - исключающее ИЛИ (^)
0 0 -> 0
0 1 -> 1
1 0 -> 1
1 1 -> 0
"""

flags4 = 9
mask4 = 1
flags4 = flags4 ^ mask4
print(flags4)  # 8, т.к.
# 9 = 00001001,
# 1 = 00000001,
# 8 = 00001000
"""ОСОБЕННОСТЬ = работа без потерь"""
flags4 = flags4 ^ mask4
print(flags4)  # 9, т.к. при применении дважды к исходной переменной мы получим исходный результат

"""
Приоритет битовый операций:
НЕ, 
И, 
ИЛИ, XOR
"""

"""
Операторы смещения бит

>> смещение бит вправо
<< смещение бит влево
"""
x = 160
print(bin(160))  # 0b10100000
x = x >> 1
print(x)  # 80 (практически тоже самое, что и деление на 2)
print(bin(x))  # 0b1010000
x = x << 1
print(x)  # 160 (практически тоже самое, что и умножение на 2)
x = x << 3
print(x)  # 1280 (160*2^3)

"""Все эти операции выполняют целочисленное умножение и деление кратное 2. 
Причем эти операции работают значительно быстрее, чем в классическом виде (x = x*2)"""