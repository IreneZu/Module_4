# Делить на 0 можно

from math import inf, nan

def divide(first, second):
    if second == 0 and first == 0:
        return nan # 'Не знаю...'
    elif second == 0:
        return inf
    else:
        return first / second
