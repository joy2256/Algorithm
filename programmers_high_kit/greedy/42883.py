# 큰 수 만들기
#뒤의 숫자보다 작으면 지우기 -> 실패
def solution_fail(number, k):
    nums = list(map(int, list(number)))
    i = 0
    while k:
        if i == len(nums) - 1:
            i = 0
        else:
            if nums[i] < nums[i + 1]:
                nums.pop(i)
                k -= 1
            else:
                i += 1
    answer = ''.join(map(str, nums))

    return answer

#힌트 -> stack 이용해보기
def solution(number, k):
    nums = list(map(int, list(number)))
    stack = []
    for num in nums:
        if k >= 0:
            if not stack: #스택이 비어 있을 경우
                stack.append(num)
            else:
                while stack and k > 0 and stack[-1] < num:
                    stack.pop()
                    k -= 1
                stack.append(num)
    # (수정) loop를 다 돌고 나서도 k > 0일때를 고려
    answer = ''.join(map(str, stack[:len(stack) - k]))
    return answer
