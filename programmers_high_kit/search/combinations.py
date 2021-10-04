def combinations(arr, r):
    result = []
    if r == 0:
        return [[]]
    for i, element in enumerate(arr):
        for c in combinations(arr[i+1:], r-1):
            result += [[element]+c]

    return result

print(combinations([1, 2, 3, 4], 2))

