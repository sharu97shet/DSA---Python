import threading
import time

def square_no(arr):
    print("calculate square nos")
    for n in arr:
        time.sleep(0.2)
        print('squ:',n*n )

    

def cube_no(arr):
    print("calculate cube nos")
    for n in arr:
        time.sleep(0.2)
        print('cube:',n*n*n )


t=time.time()
print(t)

ar=[2,4,6,8]
t1=threading.Thread(target=square_no,args=(ar,))
t2=threading.Thread(target=cube_no,args=(ar,))

t1.start()
t2.start()

t1.join()
t2.join()

# square_no(ar)
# cube_no(ar)

print("done in.. ", time.time()-t)