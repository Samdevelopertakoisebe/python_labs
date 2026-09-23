# Самбуров Георгий

# Лабораторная работа 1
## 1

![Тестовые данные](./images/lab01/img.png)

## 2

![Тестовые данные](./images/lab01/img_2.png)

## 3

![Тестовые данные](./images/lab01/img_5.png)

## 4

![Тестовые данные](./images/lab01/img_6.png)

## 5

![Тестовые данные](./images/lab01/img_8.png)

## 6

![Тестовые данные](./images/lab01/img_4.png)

## 7

![Тестовые данные](./images/lab01/img_12.png)

# Лабораторная работа 2
## 1

### min_max
![Принты](./images/lab02/img.png)
![Выводы](./images/lab02/img_1.png)
```python
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
```

### unique_sorted
![Принты](./images/lab02/img_2.png)
![Выводы](./images/lab02/img_3.png)
```python
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
```

### flatten
![Принты](./images/lab02/img_4.png)
![Выводы](./images/lab02/img_5.png)
```python
def flatten(mat):
    res = []
    for i in mat:
        if isinstance(i, (list, tuple)):
            res = res + list(i)
        else:
            raise TypeError('Toka spiski bratan')
    return res

```

## 2

![Принты](./images/lab02/img_.png)
![Выводы](./images/lab02/img_.png)

## 3

![Принты](./images/lab02/img_.png)
![Выводы](./images/lab02/img_.png)

## 4

![Принты](./images/lab02/img_.png)
![Выводы](./images/lab02/img_.png)

## 5

