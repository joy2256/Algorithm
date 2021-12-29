def permutations(arr, r):
    result = []
    if r == 0:
        return [[]]
    for i, element in enumerate(arr):
        for p in permutations(arr[:i]+arr[i+1:], r - 1):
            result += [[element]+p]
    return result

arr = [1, 2, 3, 4]
visited = [0 for _ in range(len(arr))]

def dfs_perm(depth, n, P):
    result = []
    if depth == n:
        return [P]
    else:
        for i in range(len(arr)):
            if visited[i] == True:
                continue
            visited[i] = True
            result += dfs_perm(depth+1, n, P+[arr[i]])
            visited[i] = False
    return result
print(dfs_perm(0, 2, []))



print([1]+[[]])