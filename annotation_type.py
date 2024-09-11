from math import sqrt
from typing import Optional

x_size = 10
y_size = 5


def add_numbers(x_size: int, y_size: int) -> int:
    return x_size + y_size


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return None
    root = calculate_square_root(your_number)
    return (f'Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {root}')


print('Сумма чисел: ', add_numbers(x_size, y_size))

print(calc(25.5))
