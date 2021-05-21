# 숫자를 입력하고 입력받은 숫자가
# 몇 번 박수를 치는지 알아보자

# 방법2: 컴퓨터가 생각하는 방법
a = 31
count = 0

for x in range(1, a+1):  # 30까지만 반복문 실행함
    while x:
        # if a % 10 == 3 or a % 10 == 6 or a % 10 == 9
        if x % 10 in [3, 6, 9]:
            count += 1
        x = x // 10

print(count)