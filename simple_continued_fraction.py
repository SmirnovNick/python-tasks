'''
Известно, что любую обыкновенную дробь можно записать в виде конечной простой
непрерывной дроби. Напишите программу, которая преобразует обыкновенную дробь
в последовательность коэффициентов a0, a1, ..., an

Например дроби 239/30 будет соответствовать непрерывная дробь
7 + (1 / (1 + (1/29))) соответственно, коэффициенты будут равны 7, 1 и 29.

Sample Input:
239/30

Sample Output:
7 1 29
'''
from typing import List, Optional


def simplified_fraction(
    n: int,  # numerator
    d: int,  # denominator
    s: Optional[List[int]] = []  # sequence
) -> List[int]:
    '''Converting a fraction to a sequence of coefficients.'''
    s.append(n // d)
    return simplified_fraction(d, n % d, s) if n % d else s


print(*simplified_fraction(*[int(i.strip())
      for i in input().strip().split('/')]))
