def decor(fun):
    def inner():
        print("IF:Before enhancing Function")
        fun()
        print("IF:after enhancing the function")
    return inner

@decor
def num():
    print("We will use this Function")
    print("and Will enhance this in decorator")

# resultantFunc = decor(num)
# resultantFunc()