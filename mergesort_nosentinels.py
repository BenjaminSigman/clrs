import math

def mergesort(arr):
    print(arr)
    if len(arr) == 1:
        return arr
    else:
        return merge(
            mergesort(arr[:math.floor(len(arr) / 2)]), 
            mergesort(arr[math.floor(len(arr) / 2):])
        )

def next_elem(arr_0, arr_1):
    if arr_0[0] < arr_1[0]:
        return arr_0
    else:
        return arr_1

def merge(arr_l, arr_r):
    merged = []
    while arr_l and arr_r:
        merged.append(next_elem(arr_l, arr_r).pop(0))
    if arr_l:
        merged.append(arr_l[0])
    else:
        merged.append(arr_r[0])
    return merged
