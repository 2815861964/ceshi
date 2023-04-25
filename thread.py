from threading import Thread, Lock
from time import sleep
#其他注意，Thread的daemon属性，如果为true则主程序结束啊线程一并结束

#Python 官方解释器 的每个线程要获得执行权限，必须获取一个叫 GIL （全局解释器锁） 的东西。
#这就导致了 Python 的多个线程 其实 并不能同时使用 多个CPU核心。
#所以如果是计算密集型的任务，不能采用多线程的方式。
bank = {
    'byhy': 0
}

bankLock = Lock()


# 定义一个函数，作为新线程执行的入口函数
def deposit(theadidx, amount):
    # 操作共享数据前，申请获取锁
    bankLock.acquire()

    balance = bank['byhy']
    # 执行一些任务，耗费了0.1秒
    sleep(0.1)
    bank['byhy'] = balance + amount
    print(f'子线程 {theadidx} 结束')

    # 操作完共享数据后，申请释放锁
    bankLock.release()


theadlist = []
for idx in range(10):
    thread = Thread(target=deposit,
                    args=(idx, 1)
                    )
    thread.start()
    # 把线程对象都存储到 threadlist中
    theadlist.append(thread)

for thread in theadlist:
    thread.join()

print('主线程结束')
print(f'最后我们的账号余额为 {bank["byhy"]}')