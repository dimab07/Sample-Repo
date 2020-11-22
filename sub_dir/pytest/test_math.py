def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def inc(x):
    return x + 1


def mul(x, y):
    return x * y


def pow(x, y):
    return x ** y


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(5, 2) == 3


def test_inc():
    assert inc(2) == 3


def test_mul():
    assert mul(1, 3) == 3


def test_pow():
    assert pow(3, 2) == 9
