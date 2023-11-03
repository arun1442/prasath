import time
import threading
def new(v,t):
    for i in range(v):
        time.sleep(t)
        print("i'm first")
def new2():
    for i in range(10):
        print("i'm second")
t1=threading.Thread(target=new,args=(10,2))
t2=threading.Thread(target=new2)
t1.start()
t1.join()
t2.start()
t2.join()
