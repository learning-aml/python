from multiprocessing import Process,Pool,Queue,Manager,current_process
import os
import time
import random

def write(q):
    name = current_process().name
    print("thread name: %s" %(name))
    for item in 'ABC':
        print("put %s in queue" % (item))
        q.put(item)
        time.sleep(random.random())
        
def reader(q):
   #获取当前线程的名字
    name = current_process().name
    print("thread name: %s" %(name))
    while True:
        if not q.empty():
            item = q.get()
            print("get %s from queue" % (item))
            time.sleep(random.random())
        else:
            break
            
if __name__ == "__main__":        
#    q = Queue()
#    pw = Process(target=write,args=(q,))
#    pw.start()
#    pw.join()
#    pr = Process(target=reader,args=(q,))
#    pr.start()
#    pr.join()
#    print('数据已读完')
   q = Manager().Queue()
   p1 = Pool(3)
   p1.apply(write,(q,))
   p1.apply(reader,(q,))
   p1.close()
   p1.join()
   print('data handlered over')