i = 5
def printing():
    global i
    i = i + 5
    print(i)

printing()
print(globals()['i'])
print(i)