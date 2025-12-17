import threading
import time

def print_nums():
    for i in range(1,27):
        print(f"Number:  {i}")
        time.sleep(1)

def print_letters():
    for i in range(ord('a'),ord('z')+1):
        print(f'Letters: {chr(i)}')
        time.sleep(1)


# print_nums()
# print_letters()

#creating 2 threads:
t1= threading.Thread(target=print_nums)
t2= threading.Thread(target=print_letters)

t = time.time()

#starting threads:
t1.start()
t2.start()

#wait for them to complete: 
t1.join()
t2.join()
#now they joined to the main thread

print(time.time()-t)