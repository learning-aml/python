import threading

local_thread = threading.local()

def process():
  name = local_thread.context
  print("hello, %s (in %s)" % (name, threading.current_thread().name))
  
def run(name):
  local_thread.context = name
  process()
  
t1 = threading.Thread(target=run, args=('zhangshan', ), name="t1")
t2 = threading.Thread(target=run, args=('laowang', ), name="t2")
t1.start()
t2.start()
t1.join()
t2.join()