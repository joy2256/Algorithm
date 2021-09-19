# 가장 큰 수
def solution(numbers):
    num = list(map(str, numbers))
    # 풀이참고 -> 1000이하의 수이므로 3번 반복
    num.sort(key=lambda x : x*3 ,reverse=True)
  
    return str(int(''.join(num)))
print(solution([3, 30, 34, 5, 9]))