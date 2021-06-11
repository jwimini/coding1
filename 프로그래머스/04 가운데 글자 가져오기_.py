# 가운데 글자 가져오기
def solution(s):
    # 문자열의 갯수가 홀수일 때는 (한개만 반환)
    # 5개 일때 - > index "2 / 7개 일때 - >3개
    if len(s) % 2 == 1:
        return s[len(s)//2]
    # 문자열의 갯수가 짝수일 때는 (두개를 반환)
    # 4개 일때 - > 2개
    else:
        return s[len(s) // 2-1] +  s[len(s)//2]

    return answer


s1 = "abcde"
print(solution(s1))
s2 = "qwer"
print(solution(s2))