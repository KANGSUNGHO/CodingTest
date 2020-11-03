# 완주하지 못한 선수, 프로그래머스 레벨 1

def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()
    completion.append("fault")

    for i  in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer


# # 다른 풀이(이 풀이는 조금 이상함)
# def solution(participant, completion):
#     answer = ''

#     participant.sort() # 전체인원
#     completion.sort()

#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]

#     return(participant[len(participant)-1])

# 다른 풀이
from collections import Counter

def solution(participant, compeltion):
    a = Counter(participant) - Counter(completion) # Counter(list) 메소드는 리스트를 딕셔너리 형태로 숫자를 세서 반환
                                                   # ex) list=["a","b","c","a"]
                                                   # collections.Counter(list)
                                                   # => {a:2, b:1, c:1}
    return list(a.keys())[0] 