def insertion_sort(arr):
    print(arr)
    if len(arr) == 1:
        return arr
    else:
        return insert(insertion_sort(arr[:-1]), arr[-1])

def insert(sorted_arr, elem):
    print(f'insertion of {elem} into {sorted_arr}')
    for i, x in enumerate(sorted_arr):
        print(elem<x)
        if elem < x:
            sorted_arr.insert(i, elem)
            print(sorted_arr)
            return sorted_arr
    sorted_arr.append(elem)
    print(sorted_arr)
    return sorted_arr
