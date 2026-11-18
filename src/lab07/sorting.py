def bubble_sort(nums: list) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) - 1):
            if nums[i] > nums[j + 1]:
                nums[i], nums[j + 1] = nums[j + 1], nums[i]
    return nums


def insertion_sort(nums: list) -> list:
    for i in range(1, len(nums)):
        cur = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > cur:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = cur
    return nums


def selection_sort(nums: list) -> list:
    for i in range(len(nums) - 1):
        start_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[start_index]:
                start_index = j
        nums[start_index], nums[i] = nums[i], nums[start_index]
    return nums