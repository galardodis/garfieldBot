def find_median(arr):
    arr = sorted(arr)
    if len(arr) == 0:
        return None
    elif not len(arr) % 2:
        return ((arr[len(arr) // 2]) + (arr[len(arr) // 2 - 1])) / 2
    else:
        return arr[len(arr) // 2]

print(find_median(arr = [1, 5, 2, 3, 6]))

print(find_median([100, 5, 2, 4, 3, 6]))
