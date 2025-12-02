from sort import (
    bubble_sort,
    quick_sort_int,
    heap_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
)
from benchmark import benchmark_sorts
import random


if __name__ == "__main__":
    import random

    sp1 = [random.randint(1, 300) for _ in range(50)]
    sp2 = [random.randint(1, 1000) for _ in range(500)]
    sp3 = [random.randint(1, 10000) for _ in range(2000)]
    float_arr = [random.uniform(0.0, 0.999) for _ in range(500)]
    int_arrays = {
        "small_array": sp1,
        "medium_array": sp2,
        "large_array": sp3,
    }

    float_arrays = {
        "floats": float_arr,
    }

    int_alg = {
        "bubble": bubble_sort,
        "quick": quick_sort_int,
        "heap": heap_sort,
        "counting": counting_sort,
        "radix": radix_sort,
    }

    float_alg = {
        "bucket": bucket_sort,
    }

    results = {}
    results.update(benchmark_sorts(int_arrays, int_alg))
    results.update(benchmark_sorts(float_arrays, float_alg))

    print(f"{'Array':<15}  {'Algorithm':<15}  {'Time (sec)':>15}")
    for arr_name, times in results.items():
        for algo_name, t in times.items():
            print(f"{arr_name:<15} | {algo_name:<10} | {t:15.6f}")
