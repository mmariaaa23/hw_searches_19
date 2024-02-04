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
        return quickSort(less)+equal+quickSort(greater) # конкатинируем списки
    else:  # В конце рекурсии: когда остается один элемент массива - его и возвращаем
        return array

