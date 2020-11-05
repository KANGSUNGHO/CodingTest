# 프로그래머스, 가장 큰 수

def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))  # map함수를 사용해 numbers를 문자열로 만들어줌
    numbers.sort(key = lambda x : x*3, reverse=True) # numbers의 원소는 0 이상 1000이하의 수라서 가장 작은 자릿수인
                                                     # 일의 자리수를 조건으로 세자리수로 만들어 비교
                                                     # 666, 101010, 222의 첫번째 인덱스 값을 비교함.
    print(''.join(numbers))                          # 문자열을 연결해줌

    answer = str(int(''.join(numbers)))              # int로 변환후 str해주는 이유 모든 값이 0일경우('000'을 처리하기위해)
                                                     # int로 변환한뒤 다시 str로 변
                                                     # [0,0,0,0]을 input으로 넣는다면 '0000'이 리턴되므로
                                                     # int로 변환해서 '0'으로 바꿔야함.
                                                     # 그리고 오버플로우 방지를 위해 str로 변환
    return answer


num = [6, 2, 10]
solution(num)
