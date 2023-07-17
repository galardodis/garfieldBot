def pure_intersection(arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        if arr1[i] in arr2 and arr1[i] not in ans:
            ans.append(arr1[i])
    return ans

arr1 = [1, 2, 3]
arr2 = [1, 1, 5]
pure_intersection(arr1, arr2)

arr1 = [1, 2, 3]
arr2 = [6, 7, 5]
pure_intersection(arr1, arr2)

arr2 = [1, 2, 3]
arr1 = [1, 2, 15, 3, 3]
pure_intersection(arr1, arr2)

arr1 = [1, 3, 3]
arr2 = [6, 3, 3]
pure_intersection(arr1, arr2)