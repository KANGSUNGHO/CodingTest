# 크레인 인형뽑기 게임, 프로그래머스 레벨1
# 인형을 만나면 바구니로 옮기는 로직을 구현하고, 그 다음엔 2개의 인형이 
# 연달아 모여있으면 없어지는 로직을 구현
def solution(board, moves):
    answer = 0
    bucket = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                if len(bucket) > 1 and bucket[-1] == bucket[-2]:
                    answer += 2
                    del bucket[-2:]
                break
    return answer

    # 다른 풀이

    def solution(board, moves):
        answer = 0
        ans_list = []

        for m in moves:
            for i in range(len(board)):
                if not ans_list:
                    ans_list.append(board[i][m-1])
                elif ans_list[-1] == board[i][m-1]:
                    ans_list.pop()
                    answer += 2
                else:
                    ans_list.append(board[i][m-1])
                board[i][m-1] = 0
                break
        return answer
