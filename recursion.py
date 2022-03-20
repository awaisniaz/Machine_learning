i = 0
import sys
def myfunc():
    global i
    i = i + 1
    print("geekshow")
    print(i)
    if(i == 100):
        return None
    else:
        myfunc()



myfunc()
print(sys.getrecursionlimit())
sys.setrecursionlimit(100000000)
print(sys.getrecursionlimit())