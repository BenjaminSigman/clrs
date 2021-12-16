import math

# mergesort without using sentinels. CLRS 2.3.2
# with lots of prints

def mergesort(arr):
    print(f'mergesort called on arr: {arr}')
    if len(arr) <= 1:
        return arr
    else:
        return merge(
            mergesort(arr[:math.floor(len(arr) / 2)]), 
            mergesort(arr[math.floor(len(arr) / 2):])
        )

def next_elem(arr_0, arr_1):
    if arr_0[0] < arr_1[0]:
        print(f'next elem from: {arr_0}')
        return arr_0
    else:
        print(f'next elem from: {arr_1}')
        return arr_1

def merge(arr_l, arr_r):
    merged = []
    while arr_l and arr_r:
        merged.append(next_elem(arr_l, arr_r).pop(0))
    if arr_l:
        print('right array empty')
        merged.extend(arr_l)
    else:
        print('left array empty')
        merged.extend(arr_r)
    print(f'merged: {merged}')
    return merged
