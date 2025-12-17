import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")
        
def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}")
if __name__=='__main__':
    #creating processes
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)
    t=time.time()

    #start the process:
    p1.start()
    p2.start()

    #wait for it to complete:
    p1.join()
    p2.join()

    print(time.time()-t)