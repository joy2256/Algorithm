# 전화번호 목록

# 정확도 통과, 시간초과
def solution1(phone_book):
    phone_book.sort(key = len)
    compList = []
    flag = True
    for phone in phone_book:
        if not compList:
            compList.append(phone_book[0])
        else:
            for comp in compList:
                temp = phone[0:len(comp)]
                if temp == comp:
                    flag = False
            if flag == False:
                break
            else:
                compList.append(phone)

    return flag

# sort를 통해 인접한 것들만 검사하게 함
def solution2(phone_book):
    phone_book.sort()
    flag = True
    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) < len(phone_book[i + 1]):
            if phone_book[i + 1].startswith(phone_book[i]):
                flag = False
                break
    return flag
print(solution2(["123","456","789"]))

    