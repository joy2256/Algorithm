# 베스트앨범 -> 어렵다..
import collections
def solution(genres, plays):
    answer = []
    genre_plays = {}
    
    for i in range(len(plays)):
        g = genres[i]
        p = plays[i]
        if g not in genre_plays.keys():
            genre_plays[g] = p
        else:
            genre_plays[g] += p
        genre_plays = sorted(genre_plays.items(), key=(lambda x : x[1]), reverse=True)
        
        for i in range(len(genre_plays)):
            first_play = 0
            second_play = 0
            first_play_idx = -1
            second_play_idx = -1
            for j in range(len(plays)):
                if genres[j] == genre_plays[i][0]:
                    if plays[j] > first_play:
                        second_play = first_play
                        second_play_idx = first_play_idx
                        first_play = plays[j]
                        first_play_idx = j
                    elif plays[j] > second_play:
                        second_play = plays[j]
                        second_play_idx = j
            if first_play_idx != -1:
                answer.append(first_play_idx)
            if second_play_idx != -1:
                answer.append(second_play_idx)
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))