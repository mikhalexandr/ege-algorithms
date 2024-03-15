# Task 4834
def F(X, Y, Z, W):
    return --(
            ((Z <= Y) and ((not X) <= W)) <= ((Z == W) or (Y and (not x)))
    )


print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = F(x, y, z, w)
                if not f:
                    print(x, y, z, w, f)
# ANSWER: yzwx
