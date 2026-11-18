from random import randint
from .search import *

def check_sorting(fn, trials=100) -> None:
    for _ in range(trials):
        current_test = [randint(0,1000) for _ in range(randint(1,100))]
        assert fn(current_test) == sorted(current_test)


def check_search() -> None:
    current_test = [randint(0, 1000) for _ in range(randint(1, 100))]
    target = current_test[randint(0, len(current_test) - 1)]
    assert linear_search(current_test, target) == current_test.index(target)
    assert binary_search(current_test, target) == current_test.index(target)


def check_two_sum(trials=100) -> None:
    for _ in range(trials):
        current_test = [randint(0, 1000) for _ in range(randint(1, 100))]
        index1 = randint(0, len(current_test) - 1)
        index2 = randint(0, len(current_test) - 1)
        while index2 == index1: index2 = randint(0, len(current_test) - 1)
        target_sum = current_test[index1] + current_test[index2]
        assert two_sum_brute(current_test, target_sum) == two_sum_fast(current_test, target_sum) == index1, index2