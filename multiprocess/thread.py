import threading
import time

def saySorry():
    print("hello world!")
    time.sleep(1)
    

#if __name__ == "__main__":
#    for i in range(5):
#        t = threading.Thread(target=saySorry)
#        t.start()
#        
#    print("main thread over")
#
#    while True:
#        length = len(threading.enumerate())
#        print("len:%s" %(length))
#        if length <=1:
#            break
        
        
class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print("xxx:%s" % i)
            
if __name__ == "__main__":
    t = MyThread()
    t.start()