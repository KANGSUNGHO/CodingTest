# 프로그래머스 H_index
def solution(citations):
    answer = 0
    for i in range(max(citations), 0, -1): # 큰 숫자부터 내려가면서 반복하는 이유,
                                           # h_index는 h번 이상 인용된 논문이 h개 이상일 때 h의 최댓값으로 봐야함.

        over_i = 0                          # 인용수가 h이상인 논문이 몇개인지 카운팅하기 위함

        for c in citations:                 # 논문 인용 리스트(citations)를 하나씩 돌면서, 인용수가 i보다 큰경우 over_i의 카운트를 하나씩 증가
                                            # 그 수가 i와 같아지는 순간 i를 리턴, over_i가 i이상 이기만 하면 되므로 over_i와 i가 같아지는 순간 더이상의 연산은 필요없음
            if c >= i:
                over_i += 1
            if over_i == i:
                answer = i
                return answer


c = [3,0,6,1,5]
a = solution(c)
print(a)