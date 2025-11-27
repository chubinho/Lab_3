def fibo_recursive(n: int) -> int:
    """ Рекурсивное вычисление чисел Фиббоначи """
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    elif n > 2:
        return fibo_recursive(n-2) + fibo_recursive(n - 1)
    else:
        raise ValueError()


def fibo(n: int) -> int:
    """ Вычисление чисел Фиббоначи через список """
    if n >= 1:
        sp = [0] * (n + 1)
        sp[1] = 1
        if n > 1:
            sp[2] = 1
        if n == 1 or n == 2:
            return 1
        else:
            for i in range(3, len(sp)):
                sp[i] = sp[i-1] + sp[i-2]
            return sp[n]
    elif n == 0:
        return 0
    else:
        raise ValueError()
