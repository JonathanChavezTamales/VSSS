import time
from multiprocessing import Process
from threading import Thread

val = 0

def count(x, pid):
    global val
    for i in range(x):
        print("pid", pid, " - val ", val)
        val+=1
        #print("id ", pid, " - ", i)
    return

if __name__ == '__main__':
    proc1 = Process(target=count, args=(10,1))
    proc2 = Process(target=count, args=(10,2))

    
    
    time1 = time.time() 
    
    print("begin")
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()
    print(val)
    print("end")

    time2 = time.time()
    
    print(time2-time1)

