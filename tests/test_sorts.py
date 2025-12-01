import pytest
#import random
from src.sort import (
    bubble_sort,
    quick_sort_int,
    counting_sort,
    radix_sort,
    #bucket_sort,
    heap_sort
)

@pytest.mark.parametrize("sort_function", [
    bubble_sort,
    quick_sort_int,
    counting_sort,
    radix_sort,
    heap_sort
])
class TestInegerSort:
    def test_empty_list(self,sort_function):
        assert sort_function([1]) == [1]
