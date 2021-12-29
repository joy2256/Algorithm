#상담
import sys

n = int(input())
consulting = []
for i in range(n):
    day, pay = map(int, sys.stdin.readline().split())
    consulting.append([day, pay])
answer = 0
dp = [0 for i in range(n+1)]
#뒤에서부터 dp
for i in range(n-1, -1, -1):
    if i + consulting[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i + consulting[i][0]] + consulting[i][1])

print(dp[0])          



