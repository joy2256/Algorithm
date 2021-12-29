# 연산자 끼워넣기
import sys
from itertools import permutations

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
operator_num = list(map(int, sys.stdin.readline().split()))
oper = []
for idx, num in enumerate(operator_num):
    for _ in range(num):
        oper.append(idx)
print(oper)
ans = []

#dfs 백트래킹으로 문제 다시 풀기

def operate(nums, oper):
    stack = []
    oper_left = len(oper)

    while oper_left > 0:
        if not stack:
            stack.append(nums.pop(0))
        else:
            if len(stack) == 1:
                stack.append(oper.pop(0))
            elif len(stack) == 2:
                stack.append(nums.pop(0))
            elif len(stack) == 3:
                b = stack.pop()
                op = stack.pop()
                a = stack.pop()
                # 연산
                result = 0
                if op == 0:
                    result = a + b
                elif op == 1:
                    result = a - b
                elif op == 2:
                    result = a * b
                elif op == 3:
                    if a < 0:
                        result = -(-a // b)
                    else: 
                        result = a // b
                stack.append(result)
                oper_left -= 1 

        print(stack)
        print(oper_left) 

    return stack[0]

for p in permutations(oper, N-1):
    ans.append(operate(nums, list(p)))
print(max(ans))
print(min(ans))       