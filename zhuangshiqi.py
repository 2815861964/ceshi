import time
def timeif(f):

    def wrapper(x):
        start = time.perf_counter()
        ret = f(x)
        print(time.perf_counter()-start)
        return ret
    return  wrapper

@timeif
def fuc(x):
    time.sleep(x)
@timeif
def fc2(y):
    return y*y
fuc(1)
fc2(9)