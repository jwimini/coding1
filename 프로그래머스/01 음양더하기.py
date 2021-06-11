def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        # True에 해당하는 요소(item)은 더한다
        if signs[i] is True:
            answer += absolutes[i]
        # False 에 해당하는 요소(item)은 뺀다
        else:
            answer -= absolutes[i]

    return answer


a = [4, 7, 12]
s = [True, False, True]
print(solution(a, s))
