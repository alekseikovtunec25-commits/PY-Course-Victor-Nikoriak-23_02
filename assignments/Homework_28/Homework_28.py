#Task 1
def cocktail_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        # ➜ проход слева направо ("вверх")
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # если не было обменов — массив уже отсортирован
        if not swapped:
            break

        swapped = False
        end -= 1

        # ⬅ проход справа налево ("вниз")
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1

    return arr

#Task 2
def merge(arr, left, mid, right):
    # создаём временные массивы вручную
    left_part = []
    right_part = []

    # копируем левую часть
    for i in range(left, mid + 1):
        left_part.append(arr[i])

    # копируем правую часть
    for i in range(mid + 1, right + 1):
        right_part.append(arr[i])

    i = j = 0
    k = left

    # слияние двух частей
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # остатки
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)

    merge(arr, left, mid, right)