def decor(fun):
    def inner():
        a = fun()
        add = a + 5
        return add
    return inner
@decor
def num():
    return 10
