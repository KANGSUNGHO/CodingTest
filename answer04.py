# 기능개발, 프로그래머스 레벨 1


def solution(progresses, speeds):
    answer = []
    count = 0
    days = []

    for i in range(len(progresses)):
        count = progresses[i] + speeds[i]
        if count != 100 && count < 100:
            for j in range(len(progresses)):
                count += sppeds[i]
                if count == 100:
                

    return answer
