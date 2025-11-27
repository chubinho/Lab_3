def factorial_recursive(n: int) -> int:
    """
    Алгоритм рекурсивного вычисления факториала
    """
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return factorial_recursive(n - 1) * n
    else:
        raise ValueError()


def factorial(n: int) -> int:
    """
    Создаем список, внутри которого получаем
    значения прошлых элементов
    """
    if n < 0:
        raise ValueError()

    sp = [0] * (n + 1)
    sp[0] = 1

    for i in range(1, n + 1):
        sp[i] = sp[i - 1] * i

    return sp[n]
