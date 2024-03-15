# Tasks EGE 2023
# -------------------------------------------------------------------------------------------------------------------- #
for A in range(1, 10 ** 4):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((x < A) or (y < A) or (x + 2 * y > 50)):
                flag = False
                break
    if flag:
        print(A)
        break
# ANSWER: 17
# -------------------------------------------------------------------------------------------------------------------- #
for A in range(1, 10 ** 4):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((x * y < A) or (x < y) or (9 < x)):
                flag = False
                break
    if flag:
        print(A)
        break
# ANSWER: 82
# -------------------------------------------------------------------------------------------------------------------- #
for A in range(100, 0, -1):
    flag = True
    for x in range(100, 0, -1):
        for y in range(100, 0, -1):
            if not (((x + 2 * y) > A) or (y < x) or (x < 30)):
                flag = False
                break
    if flag:
        print(A)
        break
# ANSWER: 89
# -------------------------------------------------------------------------------------------------------------------- #