# 토익시험에서 650점 이상 800점 미만의 성적을 취득한 학생만
def solution(scores):
    count = 0
    for s in scores:
        # 파이썬 문법에만 해당
        if 650 <= s < 800:
            count += 1
    return count


# The following is code to output testcase. The code below is correct and you shall correct solution function.
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

# Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
