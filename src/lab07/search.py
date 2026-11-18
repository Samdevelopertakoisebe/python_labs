def linear_search(nums: list, x: int) -> int:
    for i, num in enumerate(nums):
        if num == x:
            return i
    return -1


def binary_search(sorted_nums: list, x: int) -> int:
    low, high = 0, len(sorted_nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_nums[mid] < x:
            low = mid + 1
        elif sorted_nums[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def two_sum_brute(nums:list, target:int) -> tuple[int, int] | None:
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i + 1:]):
            if num1 + num2 == target:
                return i, j
    return None


def two_sum_fast(nums:list, target:int) -> tuple[int, int] | None:
    checked = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in checked:
            return checked[need], i
        checked[num] = i
    return None