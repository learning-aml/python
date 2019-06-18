import threading
import time


g_num=0

def worker1(lock):
    global g_num

    for x in range(200000):
        if lock.acquire():
            g_num += 1
            lock.release()
        
     
def worker2(lock):
    global g_num
    
    for x in range(200000):
        if lock.acquire():
            g_num += 1
            lock.release()    
         
lock  = threading.Lock()  
t1 = threading.Thread(target=worker1, args=(lock,))
t1.start()
t1.join()
t2 = threading.Thread(target=worker2, args=(lock, ))
t2.start()
t2.join()  
print("main thread %d " % (g_num))