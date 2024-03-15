# 3483
for A in range(1, 10 ** 4):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not (((x - 20 < A) and (20 - x < A)) or (x * y > 50)):
                flag = False
                break
    if flag:
        print(A)
        break
# ANSWER: 31
