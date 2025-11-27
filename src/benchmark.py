import timeit
from typing import Callable

def timeit_once(func, *args, **kwargs) -> float:
    """ Запускаем функцию один раз и возвращаем время выполнения"""
    timer = timeit.Timer(stmt=lambda: func(*args, **kwargs))
    res = timer.timeit(number=1)
    return res


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable[[list],list]]) -> dict[str, dict[str, float]]:
    """
    Создаем словарь результатов, после чего проходимся по словарю массивов и
    создаем по их индексу новые словари,
    куда уже будем добавлять время выполнения сортировок
    """
    results: dict[str, dict[str, float]] = {}
    for arr_name, arr in arrays.items():
        results[arr_name] = {}
        for algo_name, algo in algos.items():
            arr_copy = arr[:]
            t = timeit_once(algo, arr_copy)
            results[arr_name][algo_name] = t

    return results
