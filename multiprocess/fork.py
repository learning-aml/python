import os

pid = os.fork()

if pid < 0:
    print("fork() called failed")
elif 0 == pid:
    print("child process, pid %d, parend id %d" %(os.getpid(), os.getppid()))
else:
    print("parent process, pid:%s, childprocess id : %d" %(os.getpid(), pid))


