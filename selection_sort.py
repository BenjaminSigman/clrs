def selection_sort(arr):
    for i, x in enumerate(arr):
        minimum = x
        min_ind = i
        for j, y in enumerate(arr[i:]):
            if y < minimum:
               minimum = y
               min_ind = j + i
        arr[i], arr[min_ind] = minimum, x
    return arr
