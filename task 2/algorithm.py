def F(X, Y, Z, W):
    return --(
            Y and (X != (Z <= W))
    )


print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):

                # f = F(x, y, z, w)
                # if not f:
                #     print(x, y, z, w, f)

                # f = F(x, y, z, w)
                # if f:
                #     print(x, y, z, w, f)

                print(x, y, z, w, F(x, y, z, w))
