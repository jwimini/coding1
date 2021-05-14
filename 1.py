# a = "life"

# b = a[0:2]
# print(b)
# range(2) == range(0,2)
# a[0:2] == a[:2]

# print(a[-1]) # a[문자열의 길이 - 1]
# print(a[-2])
# print(a[-3])
# print(a[-4])

# a = "life is too short."
# print(a[3:7])
# print(a[2:])
# print(a[:9])
# print(a[:])

# a = "life is too short."
# money in the box
# b = "istoo" in a
# print(b)

# l = [1,2,3]
# print(l)
# print(l[1])

l = [1,2,3]
# l = l+[4,5]
l[2] = 0
# print(l)
# print(l*3)
print(l)
#
# arr = [1,2,3,3,1,3,3,2,3,2]
# count =[0,0,0,0]
#
# for x in arr:
#     count[x] += 1
#
# print(f"1의 갯수 : {count[1]}")
# print(f"2의 갯수 : {count[2]}")
# print(f"3의 갯수 : {count[3]}")
counter = [0, 2, 3, 5]

def 최대값(arr):  # 배열하면 반복문 생각하기
    large = 0
    for x in arr:
        if x > large:
            large = x
    return large


# 최대값(arr)