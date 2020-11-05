# k번째 수

def solution(array, commands):

    answer = []
    bucket = []

    for com in commands:
        bucket = array[com[0]-1:com[1]]
        bucket.sort()
        answer.append(bucket[com[2]-1])

        return answer
