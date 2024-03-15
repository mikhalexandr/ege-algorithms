# 6366
def F1(X, Y, Z, W):
    return --(
            (W <= Y) == (Z <= X)
    )


def F2(X, Y, Z, W):
    return --(
            (W <= Y) and ((not X) == Z)
    )


print('x y z w F1 F2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print(x, y, z, w, F1(x, y, z, w), F2(x, y, z, w))
# ANSWER yzxw
