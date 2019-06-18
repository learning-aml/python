import threading
import time


g_num=0

def worker1():
    global g_num
    for x in range(200000):
        g_num += 1
         
for i in range(2):
    t = threading.Thread(target=worker1)
    t.start()
    
print("main thread %d " % (g_num))