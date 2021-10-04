# 등굣길
def solution(m, n, puddles):
    # 맨 왼쪽과 오른쪽을 위해 한줄씩 추가해주기
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    dp[1][1] = 1 # 집
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 학교의 좌표는 (m, n), 우리는 [n][m]으로 접근함
            if [j, i] in puddles:
                continue #0인 상태
            if i == 1 and j == 1:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1] % 1000000007