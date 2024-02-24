import time
import random
import numpy as np
random_array = [random.random() for _ in range(200)]  # Random floats between 0 and 1
print("The original array is : ")
print(random_array)

#lis=[20,10,5,35,64,89,2,4,6]

start=time.time_ns()
random_array.sort()
end=time.time_ns()

print("The sorted array is : ",random_array)
print("Execution time : ",end-start)



