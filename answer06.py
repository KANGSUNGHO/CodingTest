# 프로그래머스 레벨1, 2016년

def solution(a,b):
    answer = ''
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]

    return day[(sum(month[:a-1]) + b ) % 7]


# 다른 풀이

import datetime


def solution(a,b):
    day_of_the_week = ['MON','TUE', 'WED','THU','FRI','SAT','SUN']
    return day_of_the_week[datetime.datetime(2016,a,b).weekday()]
    # datetime 모듈에서 datetime 으로 날짜 생성 후 weekday 함수로 요일을 찾는다.
    # 요일은 숫자로 반환되니 리스트에 월 ~ 일을 생성 후 출력하도록 함.
    # 월요일 = 0, 일요일 = 6


