# __*__ coding:utf-8 __*__
import asyncio
import threading
import time


@asyncio.coroutine
def hello1():
    print('Hello,world,start...1...%s' % threading.currentThread())
    # 异步调用asyncio.sleep(3):
    r = yield from asyncio.sleep(3)
    print('Hello world,end...1...%s' % threading.currentThread())


@asyncio.coroutine
def hello2():
    print('Hello,world,start...2...%s' % threading.currentThread())
    # 异步调用asyncio.sleep(5):
    r = yield from asyncio.sleep(5)
    print('Hello world,end...2...%s' % threading.currentThread())


# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
task = [hello1(), hello2()]
starttime = time.time()
loop.run_until_complete(asyncio.wait(task))
loop.close()
print('用时：%.5f秒' % float(time.time()-starttime))
