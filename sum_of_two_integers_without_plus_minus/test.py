def negate(a):
    if a < 0:
        a = ~a
        a = AddTwoPositive(a, 1)
    elif a > 0:
        a = subtractTwoPositive(a, 1)
        a = ~a
    return a


def AddTwoPositive(x, y):
    if (y == 0):
        return x
    else:
        return AddTwoPositive(x ^ y, (x & y) << 1)


def subtractTwoPositive(x, y):
    if y > x:
        return negate(subtractTwoPositive(y, x))
    if (y == 0):
        return x
    else:
        return subtractTwoPositive(x ^ y, (~x & y) << 1)


def Add(x, y):
    print(x, y)
    if x*y > 0:
        if x < 0:
            return negate(AddTwoPositive(negate(x), negate(y)))
        else:
            return AddTwoPositive(x, y)
    else:
        if y < 0:
            return subtractTwoPositive(x, negate(y))
        else:
            return subtractTwoPositive(y, negate(x))


print(Add(32, 12))
