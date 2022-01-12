#Note: We are looking for a single instance of the element

def binary_search(arr, elem, start_ind, end_ind):
    if start_ind <= end_ind:
        mid = (start_ind + end_ind) // 2
        if arr[mid] == elem:
            return mid
        elif arr[mid] < elem:
            return binary_search(arr, elem, mid + 1, end_ind)
        else:
            return binary_search(arr, elem, start_ind, mid - 1)
    else:
        return -1
