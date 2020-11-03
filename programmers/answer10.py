# 프로그래머스 레벨1,
# 입력된 수가 짝수라면 2로 나눔
# 입력된 수가 홀수라면 3을 곱하고 1을 더함
# 결과로 나온 수에 같은 작업을 1이 될 때까지 반복
# num은 1 이상 800000000미만인 정수
# 작업을 500번을 반복해도 1이 되지 않으면 -1을 반환

def solution(num):
    i = 0
    answer = 0
    while num > 1 and num != 1:
        if num % 2 == 0:
            num  = num / 2
            answer = += 1
        else:
            num = num * 3 + 1
            answer += 1
        i += 1
        if i > 499:
            answer = -1
            return answer
    return answer