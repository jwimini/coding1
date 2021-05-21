def solution(number):
    count = 0
    for i in range(1, number + 1):  # for(int i=1; i<number+1)
        current = i
        temp = count
        while current != 0:
            if current % 10 % 3 ==0 and current%10 !=0:
                count += 1
            current = current // 10
        return count


# The following is code to output testcase.
number = 40
ret = solution(number)
print(ret)
