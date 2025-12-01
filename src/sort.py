def bubble_sort(a: list[int]) -> list[int]:
    """Уставнавливаем флаг, который указывает, что
    перестановка была за проход,
    после этого проходимся по элементам и сравниваем два
    соседних элемента
    """
    if not isinstance(a, list):
        raise TypeError("Input should be a list")
    if len(a) < 2:
        return a
    if not all(isinstance(x, int) for x in a):
        raise TypeError("Each element must be an integer")
    if any(x < 0 for x in a):
        raise ValueError("Each element must be more than 0")
    sp = a[:]
    flag = True
    while flag:
        flag = False
        for i in range(len(sp) - 1):
            if sp[i] > sp[i+1]:
                sp[i], sp[i+1] = sp[i+1], sp[i]
                flag = True

    return sp


def quick_sort_int(a: list[int]) -> list[int]:
    """
    Выбираем последний элемент, после чего
    создаем 3 списка: элементы меньшие нашего элемента,
    равные ему, и большие его. После чего
    рекурсивно вызываем быструю сортировку уже
    для элементов, меньнших и больших нашего числа
    """
    if len(a) < 2:
        return a
    if not isinstance(a, list):
        raise TypeError("Input should be a list")
    if not all(isinstance(x, int) for x in a):
        raise TypeError("Each element must be an integer")
    if any(x < 0 for x in a):
        raise ValueError("Each element must be more than 0")
    sp = a[:]
    if len(sp) <= 1:
        return sp
    pivot = sp[-1]
    left_pivot = [x for x in sp if x < pivot]
    middle_pivot = [x for x in sp if x == pivot]
    right_pivot = [x for x in sp if x > pivot]

    return quick_sort_int(left_pivot) + middle_pivot + quick_sort_int(right_pivot)


def quick_sort_float(a: list[float]) -> list[float]:
    """
    Выбираем последний элемент, после чего
    создаем 3 списка: элементы меньшие нашего элемента,
    равные ему, и большие его. После чего
    рекурсивно вызываем быструю сортировку уже
    для элементов, меньнших и больших нашего числа
    """
    if len(a) < 2:
        return a
    if not isinstance(a, list):
        raise TypeError("Input should be a list")
    if not all(isinstance(x, float) for x in a):
        raise TypeError("Each element must be a float")
    if any(x < 0 for x in a):
        raise ValueError("Each element must be more than 0")
    sp = a[:]
    if len(sp) <= 1:
        return sp
    pivot = sp[-1]
    left_pivot = [x for x in sp if x < pivot]
    middle_pivot = [x for x in sp if x == pivot]
    right_pivot = [x for x in sp if x > pivot]

    return quick_sort_float(left_pivot) + middle_pivot + quick_sort_float(right_pivot)


def counting_sort(a: list[int]) -> list[int]:
    """Создаем массив состоящий из нулей, после чего
    добавляем в него по индексу
    (индекс это текущее значение - минимальное число),
    после его проходимся по этом списку и пока текущее
    значение не ноль, то добавляем текущий индекс +
    минимальное значение в список результата
    """
    if len(a) < 1:
        return []
    if not isinstance(a, list):
        raise TypeError("Input should be a list")
    if not all(isinstance(x, int) for x in a):
        raise TypeError("Each element must be an integer")
    if any(x < 0 for x in a):
        raise ValueError("Each element must be more than 0")
    sp = a[:]
    max_sp = max(sp)
    min_sp = min(sp)
    count = [0] * (max_sp - min_sp + 1)
    for i in range(len(sp)):
        count[sp[i] - min_sp] += 1
    sp = []
    for i in range(len(count)):
        sp.extend([i + min_sp] * count[i])
    return sp


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Берем максимальный элемент списка, после чего
    запускаем цикл пока максимальное число деленное на заданное значение
    больше 0, то сортируем по последнему числу и затем сортируем по самому
    левому числу массива
    """
    if not isinstance(a, list):
        raise TypeError("Input should be a list")
    if not all(isinstance(x, int) for x in a):
        raise TypeError("Each element must be an int")
    if any(x < 0 for x in a):
        raise ValueError("Each element must be more than 0")
    if base < 2:
        raise ValueError("Base must be >= 2")
    sp = a[:]
    if not sp:
        return sp
    max_arr = max(sp)
    exp = 1
    while max_arr // exp > 0:
        buckets: list[list[int]] = [[] for _ in range(base)]
        for num in sp:
            index = (num // exp) % base
            buckets[index].append(num)
        sp = [num for bucket in buckets for num in bucket]
        exp *= base

    return sp


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
    Создаем корзины, в которые потом добавляем занчения по
    логике нахождени индекса(это целая часть
    от умножения текущего знаения на количество корзин),
    после этого каждая корзина сортируется с помощью
    quick_sort и дополняет список вывода.
    """
    if not isinstance(a, list):
        raise TypeError("Input should be a list")
    if not all(isinstance(x, float) for x in a):
        raise TypeError("Each element must be a float")
    if any(not (0 <= x < 1) for x in a):
        raise ValueError("The value in bucket_sort should be in [0, 1)")
    if len(a) < 2:
        return a[:]
    arr = a[:]
    length = len(arr)
    bucket_count = buckets if buckets is not None else length
    if bucket_count < 1:
        bucket_count = 1

    buckets_list: list[list[float]] = [[] for _ in range(bucket_count)]
    for x in arr:
        index = int(x * bucket_count)
        if index >= bucket_count:
            index = bucket_count - 1
        buckets_list[index].append(x)
    result = []
    for bucket in buckets_list:
        if len(bucket) > 1:
            result.extend(quick_sort_float(bucket))
        else:
            result.extend(bucket)

    return result


def heapify(sp, n, i):
    """
    Всопомогательная функция для heap_sort,
    которая выявляет максимальный элемент из трех
    и выводит его наверх двоичного поддерева.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and sp[left] > sp[largest]:
        largest = left
    if right < n and sp[right] > sp[largest]:
        largest = right
    if largest != i:
        sp[i], sp[largest] = sp[largest], sp[i]
        heapify(sp, n, largest)


def heap_sort(a: list[int]) -> list[int]:
    """
    Идем с середины влево по списку, тк именно эти элементы имеют
    дочерние элементы последнего уровня снизу,
    поэтому с помощью них мы поднимаемся всё выше
    и выше, формируя max-heap
    """
    if not isinstance(a, list):
        raise TypeError("Input should be a list")
    if not all(isinstance(x, int) for x in a):
        raise TypeError("Each element must be an int")
    if any(x < 0 for x in a):
        raise ValueError("Each element must be more than 0")
    sp = a[:]
    n = len(sp)

    for i in range(n // 2 - 1, -1, -1):
        heapify(sp, n, i)

    for i in range(n - 1, 0, -1):
        sp[0], sp[i] = sp[i], sp[0]
        heapify(sp, i, 0)

    return sp
