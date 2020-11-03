# 프로그래머스, 레벨 1 문자열 내림차순 정렬

def solution(s):
    answer = ''
    return "".join(reversed(sorted(s)))


# 다른 풀이

def solution(s):
    answer = ''
    
    return "".join(sorted(s)[::-1])


# 다른 풀이
def solution(s):
    return "".join(sorted(s,reverse=True)

