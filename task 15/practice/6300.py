# 6300
for A in range(1, 10 ** 4):
    flag = True
    for x in range(1, 1000):
        if not (((x & 112 != 0) or (x & 86 != 0)) <= ((x & 65 == 0) <= (x & A != 0))):
            flag = False
            break
    if flag:
        print(A)
        break
# ANSWER: 54
