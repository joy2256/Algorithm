#삼성 응시테스트 홀짝 카드놀이

def get_max_score(card_arr):
    odd_cards = []
    even_cards = []
    score = 0
    for card in card_arr:
        if card % 2 == 1:
            odd_cards.append(card)
        else:
            even_cards.append(card)
    odd_cards.sort()
    even_cards.sort()
    if len(odd_cards) % 2 == 0:
        #짝, 홀수 각각 뽑기
        for card in odd_cards[(len(odd_cards)//2):]:
            score += card
        for card in even_cards[(len(even_cards)//2):]:
            score += card
    else:
        for card in odd_cards[(len(odd_cards)//2 + 1):]:
            score += card
        for card in even_cards[(len(even_cards)//2 + 1):]:
            score += card
        score += min(odd_cards[len(odd_cards)//2], even_cards[len(even_cards)//2])
    return score

test_num = int(input())
score = []
for i in range(test_num):
    n = int(input())
    cards = list(map(int, input().split()))
    score.append(get_max_score(cards))
for i in range(test_num):
    print('#%d' % (i+1), score[i])


            