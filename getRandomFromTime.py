import time
def f(x):
  while 1:
    t1=time.time()
    time.sleep(x)
    t2=time.time()
    print(t2-t1)
    print(str(t2-t1))
    