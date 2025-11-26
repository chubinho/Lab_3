def bubble_sort(a: list) -> list:
    sp = a[:]
    flag = True
    while flag:
        flag = False
        for i in range(len(sp) - 1):
            if sp[i] > sp[i+1]:
                sp[i], sp[i+1] = sp[i+1], sp[i]
                flag = True
    return sp


def quick_sort(a: list) -> list:
    sp = a[:]
    if len(sp) <= 1:
        return sp
    pivot = sp[-1]
    left_pivot = [x for x in sp if x < pivot]
    middle_pivot = [x for x in sp if x == pivot]
    right_pivot = [x for x in sp if x > pivot]
    return quick_sort(left_pivot) + middle_pivot + quick_sort(right_pivot)


def counting_sort(a: list) -> list:
    sp = a[:]
    max_sp = max(sp)
    min_sp = min(sp)
    count = [0] * (max_sp - min_sp + 1)
    for i in range(len(sp)):
        count[sp[i] - min_sp] += 1
    sp = []
    for j in range(len(count)):
        while count[j] > 0:
            sp.append(j - min_sp)
            count[j] -= 1
    return sp


def radix_sort(a: list[int], base: int = 10) -> list[int]:
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
    if len(a) <= 1:
        return a[:]

    arr = a[:]
    n = len(arr)

    if buckets is None:
        buckets = n

    else:
        bucket_count = buckets

    if bucket_count < 1:
        bucket_count = 1

    min_val = min(arr)
    max_val = max(arr)

    if min_val == max_val:
        return arr

    buckets_list: list[list[float]] = [[] for _ in range(bucket_count)]

    delta = max_val - min_val
    for x in arr:
        index = int((x - min_val) * bucket_count / delta)
        if index == bucket_count:
            index -= 1
        buckets_list[index].append(x)

    result = []
    for bucket in buckets_list:
        if len(bucket) > 1:
            result.extend(quick_sort(bucket))
        else:
            result.extend(bucket)

    return result


def heapify(sp, n, i):
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
    sp = a[:]
    n = len(sp)

    for i in range(n // 2 - 1, -1, -1):
        heapify(sp, n, i)

    for i in range(n - 1, 0, -1):
        sp[0], sp[i] = sp[i], sp[0]
        heapify(sp, i, 0)

    return sp
