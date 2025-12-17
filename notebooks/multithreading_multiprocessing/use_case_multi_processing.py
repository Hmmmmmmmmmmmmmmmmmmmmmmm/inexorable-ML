'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation 
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across 
multiple CPU cores, improving performance.
'''

import multiprocessing
import math
# import sys
import time

#increasing the maximum numbers of digits for int conversion
# sys.set_int_max_str_digits(100000)

#function for factorial:

def compute_factorial(num):
    print(f"Computing factorial of {num}")
    result = math.factorial(num)
    print(f"Factorial of {num} is {result}")
    return result

if __name__ == '__main__':
    numbers=[5000,6000,7000,8000,9000]

    start_time = time.time()

    #creating a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial,numbers)
    
    end_time = time.time()

    print(f"Results:    {results}")
    print(f"Time Taken: {end_time-start_time} seconds")
