import pytest
import random
from src.sort import (
    bubble_sort,
    quick_sort_int,
    counting_sort,
    radix_sort,
    bucket_sort,
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
    def test_empty_list(self, sort_function):
        assert sort_function([]) == []

    def test_only_one_element(self, sort_function):
        assert sort_function([1]) == [1]

    def test_simple_lists(self, sort_function):
        sp1 = [1, 2, 415, 35325, 153, 515, 51, 545, 3453]
        sp2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sp3 = [x for x in range(1000, 100, -1)]
        sp4 = [random.randint(0, 10**4) for _ in range(100)]
        assert sort_function(sp1) == sorted(sp1)
        assert sort_function(sp2) == sorted(sp2)
        assert sort_function(sp3) == sorted(sp3)
        assert sort_function(sp4) == sorted(sp4)

    def test_already_sorted(self, sort_function):
        sp1 = [50, 60, 70, 80, 90, 100000, 200000, 500000]
        sp2 = [x for x in range(100, 10**3)]
        assert sort_function(sp1) == sorted(sp1)
        assert sort_function(sp2) == sorted(sp2)

    def test_error_non_list(self, sort_function):
        with pytest.raises(TypeError, match="Input should be a list"):
            sort_function("      ")
        with pytest.raises(TypeError, match="Input should be a list"):
            sort_function("!!!!!!!!!!!!!!!!!!!!!")
        with pytest.raises(TypeError, match="Input should be a list"):
            sort_function("Acvfvfv")

    def test_non_integer_elements(self, sort_function):
        with pytest.raises(TypeError, match="Each element must be an int"):
            sort_function([1, 2, 4, 5, 6, "414141"])
        with pytest.raises(TypeError, match="Each element must be an int"):
            sort_function([25, 141, 0.00001])
        with pytest.raises(TypeError, match="Each element must be an int"):
            sort_function(["13", "dadadadad"])

    def test_non_positive_integer(self, sort_function):
        with pytest.raises(ValueError, match="Each element must be more than 0"):
            sort_function([1, 2, 4, -5])


class TestBucketSort:
    def test_empty_list(self):
        assert bucket_sort([]) == []

    def test_only_one_element(self):
        assert bucket_sort([0.5]) == [0.5]

    def test_simple_lists(self):
        sp1 = [000.1, 0.2, 0.1, 0.000009, 0.849289423, 0.1312414144]
        sp2 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1]
        sp3 = [x / 1000 for x in range(900, 1, -1)]
        sp4 = [random.uniform(0, 0.99999) for _ in range(100)]
        assert bucket_sort(sp1) == sorted(sp1)
        assert bucket_sort(sp2) == sorted(sp2)
        assert bucket_sort(sp3) == sorted(sp3)
        assert bucket_sort(sp4) == sorted(sp4)

    def test_already_sorted(self):
        sp1 = [0.5, 0.60, 0.70, 0.80, 0.90, 0.100000, 0.200000, 0.500000]
        sp2 = [0.1, 0.11, 0.11111, 0.1111111]
        assert bucket_sort(sp1) == sorted(sp1)
        assert bucket_sort(sp2) == sorted(sp2)

    def test_error_non_list(self):
        with pytest.raises(TypeError, match="Input should be a list"):
            bucket_sort("      ")
        with pytest.raises(TypeError, match="Input should be a list"):
            bucket_sort("!!!!!!!!!!!!!!!!!!!!!")
        with pytest.raises(TypeError, match="Input should be a list"):
            bucket_sort("Acvfvfv")

    def test_non_float_elements(self):
        with pytest.raises(TypeError, match="Each element must be a float"):
            bucket_sort([0.1, 0.2, 0.4, 0.5, 0.6, "414141"])
        with pytest.raises(TypeError, match="Each element must be a float"):
            bucket_sort([0.25, 0.141, 1])
        with pytest.raises(TypeError, match="Each element must be a float"):
            bucket_sort(["13", "dadadadad"])

    def test_non_positive_floats(self):
        with pytest.raises(ValueError, match="The value in bucket_sort should be in"):
            bucket_sort([0.1, 0.2, 0.4, -0.5])
