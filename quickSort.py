def quickSort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quickSort(less) + equal + quickSort(greater)  # конкатинируем списки
    else:  # В конце рекурсии: когда остается один элемент массива - его и возвращаем
        return array


# сложность по времени - O(n log n) (худший случай O(n^2)) - т. к каждый раз мы делим "несортированную часть" на 2
# сложность по памяти - O(3n) -> O(n) 
