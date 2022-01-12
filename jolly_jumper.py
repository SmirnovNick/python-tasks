'''
Последовательность n>0 целых чисел называется jolly jumper в случае, если
значения абсолютных разностей последовательных элементов принимают все
возможные значения между 1 и n-1.
Например, последовательность 1, -3, -4, -1, 1 является jolly jumper
последовательностью, так как абсолютные разности равны 4, 1, 3, 2,
соответственно, а n-1=4.
Будем считать, что последовательность из одного числа является jolly jumper.

Напишите программу, которая проверяет, является ли введённая
последовательность jolly jumper.

Формат ввода:
Строка, содержащая 1≤n≤10000
целых чисел, разделённых пробелом.

Формат вывода:
Одна строка, содержащая "Jolly" (без кавычек), если последовательность является
jolly jumper и "Not jolly" в противном случае.
'''
from typing import List, Set

input_str: str = input().strip()
num_list: List[int] = [int(i.strip()) for i in input_str.split(' ')]
num_count: int = len(num_list)

if num_count == 1:
    print('Jolly')
else:
    abs_diff: Set[int] = {abs(num_list[i] - num_list[i + 1])
                          for i in range(num_count - 1)}

    if len(set(range(1, num_count)) - abs_diff) == 0:
        print('Jolly')
    else:
        print('Not jolly')
