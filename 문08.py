def solution(char):
    result = ""
    result += char[0]
    for i in range(1, len(char)):
        if char[i - 1] != char[i]:
            result += char[i]

    return result
char = "abcdefg"
ret = solution(char)
