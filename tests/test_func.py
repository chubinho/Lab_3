import pytest
from src.fibo import fibo_recursive, fibo
from src.factorial import factorial,factorial_recursive


@pytest.mark.parametrize("factorial_func", [factorial_recursive, factorial])
class TestFactorial:
    def test_correct_inputs(self, factorial_func):
        assert factorial_func(0) == 1
        assert factorial_func(5) == 120
        assert factorial_func(10) == 3628800

    def test_invalid_inputs(self, factorial_func):
        with pytest.raises(ValueError, match="The number must be natural"):
            factorial_func(-1)
        with pytest.raises(ValueError, match="The number must be natural"):
            factorial_func("5")


@pytest.mark.parametrize("fibo_func", [fibo_recursive, fibo])
class TestFibonacci:
    def test_correct_inputs(self, fibo_func):
        assert fibo_func(0) == 0
        assert fibo_func(1) == 1
        assert fibo_func(10) == 55

    def test_invalid_inputs(self, fibo_func):
        with pytest.raises(ValueError, match="The number must be natural"):
            fibo_func(-1)
        with pytest.raises(ValueError, match="The number must be natural"):
            fibo_func("10")


def test_compare_func():
    for n in range(20):
        assert factorial_recursive(n) == factorial(n)
        assert fibo_recursive(n) == fibo(n)
