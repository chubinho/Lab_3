import pytest
import random
from src.sort import (
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
    heap_sort
)


def rand_int(lo=0, hi=10000):
    return random.randint(lo, hi)

def rand_float():
    return random.uniform(0.0, 0.999999)


@pytest.mark.parametrize("arr", [
    [],
    [5],
    [2, 1],
    [3, 1, 4, 1, 5],
    [10, -5, 0, 3, -1],
    [1, 1, 1],
    list(range(10, 0, -1)),
] + [[rand_int() for _ in range(random.randint(0, 50))] for _ in range(10)])
def test_bubble_sort(arr):
    assert bubble_sort(arr.copy()) == sorted(arr)


@pytest.mark.parametrize("arr", [
    [],
    [42],
    [5, 2, 8, 1],
    [-3, -1, 0, 2, 5],
    [7, 7, 7],
    list(range(100, 90, -1)),
] + [[rand_int() for _ in range(random.randint(0, 50))] for _ in range(10)])
def test_quick_sort(arr):
    assert quick_sort(arr.copy()) == sorted(arr)


@pytest.mark.parametrize("arr", [
    [0],
    [5, 2, 9, 1, 3],
    [100, 100, 100],
    list(range(50, 151)),
] + [[rand_int(0, 400) for _ in range(random.randint(0, 50))] for _ in range(10)])
def test_counting_sort(arr):
    assert counting_sort(arr.copy()) == sorted(arr)


@pytest.mark.parametrize("arr", [
    [],
    [0],
    [1, 2, 3],
    [170, 45, 75, 90, 802, 24, 2, 66],
    [0, 100, 50, 1],
    [999, 1, 10, 100, 500],
] + [[rand_int(0, 1000) for _ in range(random.randint(0, 50))] for _ in range(10)])
def test_radix_sort(arr):
    assert radix_sort(arr.copy()) == sorted(arr)


@pytest.mark.parametrize("arr", [
    [],
    [0.5],
    [0.1, 0.9, 0.3, 0.7],
    [0.0, 0.999999, 0.5],
    [0.25, 0.25, 0.25],
    [i / 100 for i in range(100)],
] + [[rand_float() for _ in range(random.randint(0, 50))] for _ in range(10)])
def test_bucket_sort(arr):
    assert bucket_sort(arr.copy()) == sorted(arr)


@pytest.mark.parametrize("arr", [
    [],
    [100],
    [3, 1, 4, 1, 5],
    [-10, -5, 0, 5, 10],
    [1, 1, 1],
    list(range(50, 0, -1)),
] + [[rand_int() for _ in range(random.randint(0, 50))] for _ in range(10)])
def test_heap_sort(arr):
    assert heap_sort(arr.copy()) == sorted(arr)
