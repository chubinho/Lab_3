def factorial_recursive(n: int) -> int:
    """
    Алгоритм рекурсивного вычисления факториала
    """
    if not isinstance(n,int) or n < 0:
        raise ValueError("The number must be natural")
    if n == 1 or n == 0:
        return 1
    else:
        return factorial_recursive(n - 1) * n



def factorial(n: int) -> int:
    """
    Создаем список, внутри которого получаем
    значения прошлых элементов
    """
    if not isinstance(n,int) or n < 0:
        raise ValueError("The number must be natural")

    sp = [0] * (n + 1)
    sp[0] = 1

    for i in range(1, n + 1):
        sp[i] = sp[i - 1] * i

    return sp[n]
