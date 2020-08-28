# 프로그래머스 레벨1, 체육복
def solution(n, lost, reserve):
    # 체육복을 빌려줄 수 있는 친구
    set_reserve = set(reserve) - set(lost) # 체육복을 빌려줄 수 있는 친구 - 체육복을 잃어버린 친구 => 진짜로 빌려줄 수 있는 친구
    set_loss = set(loss) - set(reserve) # 체육복을 잃어버린 친구 - 체육복 여분이 있는 친구 => 진짜 체육복이 없는 친구
    for i in set_reserve:
        if i-1 in set_loss:
            set_loss.remove(i-1)
        elif i+1 in set_loss:
            set_loss.remove(i+1)

    return n - len(set_loss)
