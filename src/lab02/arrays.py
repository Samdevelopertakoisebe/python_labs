def min_max(nums):
    maxx, minn = -2**63, 2**63
    if len(nums) == 0:
        raise ValueError
    for x in nums:
        if x > maxx:
            maxx = x
        if x < minn:
            minn = x
    return maxx, minn

def unique_sorted(nums):
    nums = list(set(nums))
    changed = True
    while changed:
        changed = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                changed = True
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

def flatten(mat):
    res = []
    for i in mat:
        if isinstance(i, (list, tuple)):
            res = res + list(i)
        else:
            raise TypeError('Toka spiski bratan')
    return res

# # min_max
# print(min_max([3, -1, 5, 5, 0]))
# print(min_max([42]))
# print(min_max([-5, -2, -9]))
# try:
#     print(min_max([]))
# except ValueError:
#     print('ValueError raised')
# print(min_max([1.5, 2, 2.0, -3.1]))

# # unique_sorted
# print(unique_sorted([3,1,2,1,3]))
# print(unique_sorted([]))
# print(unique_sorted([-1,-1,0,2,2]))
# print(unique_sorted([1.0,1,2.5,2.5,0]))

# # unique_sorted
# print(flatten([[1, 2], [3, 4]]))
# print(flatten([[1, 2], (3, 4, 5)]))
# print(flatten([[1], [], [2, 3]]))
# print(flatten([[1, 2], "ab"]))