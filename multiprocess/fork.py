import os
import time

pid = os.fork()
num = 100

if pid < 0:
    print("fork() called failed")
elif 0 == pid:
    time.sleep(2)
    num +=1
    print("child process, pid %d, parend id %d, num: %d" %(os.getpid(), os.getppid(), num))
else:
    print("parent process, pid:%s, childprocess id : %d, num:%d" %(os.getpid(), pid, num))


