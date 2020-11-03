# 프로그래머스 레벨1, 모의고사
def solution(answers):
    friend1 = [1,2,3,4,5]
    friend2 = [2,1,2,3,2,4,2,5]
    friend3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]

    for id, answer in enumerate(answers): # enumerate 반복문 사용시 몇번째 반복문이지 확인이 필요한데 이때 사용.
                                          # 인덱스 번호와 컬렉션의 원소를 tuple 형태로 반환함.
                                          # t = [1,5,7]
                                          # for p in enumerate(t):
                                          #    print(p)
                                          #  => (0,1),(1,5),(2,7) 
        if answer == friend1[id%len(friend1)]: # idfmf lend(friend1)로 나눈 나머지 값을 구하는 이유
                                               # answer의 해당 요소가 각 friend가 가지고 있는 패턴 중 몇번째 인덱스와
                                               # 비교해야 하는지를 알아야 하기 때문
                                               # ex) friend1은 [1,2,3,4,5,1,2,3,4,5...]로 5개의 숫자를 패턴으로 찍기를 하는데
                                               # anwer가 [1,3,2,4,2,3,5,1]로 비교해야할 문제 8문제가 주어졌다면
                                               # enumerate 함수를 통해 id, answer=(0,1),(1,3),(2,2),(3,4),(4,2),(5,3),(6,5),(7,1)이 됨
                                               # 마지막 8번째 문제(인덱스 7)를 비교해보면 정답은 1, friend1이 찍은 숫자는 1,2,3,4,5,1,2,3 즉 3이 되어야함.
                                               # 1,2,3,4,5 중 3은 2번째 인덱스이고 이를 구하기 위한 과정이 id %len(friend1)임.
            score[0] += 1
        if answer == friend2[id%len(friend2)]:
            score[1] += 1
        if answer == friend3[id%len(friend3)]:
            score[2] += 1

        return [i+1 for i in range(3) if socre[i] == max(score)]

