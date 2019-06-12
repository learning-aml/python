from multiprocessing import Process
import os
import time

class  Task(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval=interval
    
    def run(self):
        print("child process: %s, parent process: %s" %(os.getpid(), os.getppid()))
        t_start=time.time()
        time.sleep(self.interval)
        t_stop=time.time()
        print("%s execution time, use %s0.2 second" %(os.getpid(), t_stop-t_start))
        
        
def func(name):
    print("child , name=%s, pid=%d " % (name, os.getpid()))

if __name__ == "__main__":
#    proc = Process(target=func, args=('test',))
#    print("run process")
#    proc.start()
#    proc.join()
#    print("run child process end")
    t_start=time.time()
    p1 = Task(2)
    p1.start()
    p1.join()
    t_stop=time.time()
    print("%s execution time, use %s0.2 second" %(os.getpid(), t_stop-t_start))
    
     
    
    
    
