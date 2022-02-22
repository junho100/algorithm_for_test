def b_search_with_loop(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            end = mid -1
            continue

        if arr[mid] < target:
            start = mid + 1
            continue
    return None

def b_search_with_recur(arr, target, start, end):
    if start <= end:
        return None
    
    mid = (start + end) // 2

    if target == arr[mid]:
        return mid

    if arr[mid] > target:
        return b_search_with_recur(arr, target, start, mid - 1)
    elif arr[mid] < target:
        return b_search_with_recur(arr, target, mid + 1, end)
    
